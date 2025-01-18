from django.shortcuts import render
from rest_framework import generics, status
from website.models import Product, Feedback
from .serializers import ProductSerializer, FeedbackSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
from ml_model.sentiment_analysis_model import sentiment_analysis

#api view for product name autocomplete
@api_view(['GET'])
def product_name_autocomplete(request):
    # Get the query from the request
    query = request.GET.get('q', '')
    #check if the data entered by the user matches any of the data in database
    products = Product.objects.filter(Q(name__icontains=query))  # case insensitive
    #Serialize the products
    serializer = ProductSerializer(products, many=True)
    #return data to frontend
    return Response(serializer.data)


 #API view for submitting feedback 
@api_view(['POST'])
def submit_feedback(request):
    print(f"Request data: {request.data}")
    #initialize serializer with incoming data
    serializer = FeedbackSerializer(data=request.data, context={'request': request})
    
    # perform sentiment analysis only if data in serializer is valid
    if serializer.is_valid():
        #serializer contains customer and product details and feedback sent from frontend
        #extract feedback for sentiment analysis
        feedback_text = serializer.validated_data['feedback_text']

        #perform sentiment analysis on feedback text
        sentiment = sentiment_analysis(feedback_text)  
        # save the sentiment analysis result into database
        feedback = serializer.save(sentiment=sentiment)
        
        #Return the sentiment analysis result to the customer 
        return Response({
            'sentiment': sentiment, 
           
        }, status=status.HTTP_201_CREATED)
    # If the serializer is not valid, return the errors with a 400 status code
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)