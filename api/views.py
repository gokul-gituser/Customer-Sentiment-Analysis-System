from django.shortcuts import render
from rest_framework import generics, status
from website.models import Product, Feedback
from .serializers import ProductSerializer, FeedbackSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
from ml_model.sentiment_analysis_model import sentiment_analysis

@api_view(['GET'])
def product_name_autocomplete(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(Q(name__icontains=query))  # Search for products containing the query
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def submit_feedback(request):
    print(f"Request data: {request.data}")
    serializer = FeedbackSerializer(data=request.data, context={'request': request})
    

    if serializer.is_valid():
        # perform sentiment analysis
        feedback_text = serializer.validated_data['feedback_text']
        sentiment = sentiment_analysis(feedback_text)  
        
        
        feedback = serializer.save(sentiment=sentiment)
        
        return Response({
            'sentiment': sentiment, 
           
        }, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)