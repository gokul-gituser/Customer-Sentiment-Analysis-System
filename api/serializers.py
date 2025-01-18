from rest_framework import serializers
from website.models import Customer,Product, Feedback

#Serializer for Product model,used for product name autocomplete
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']  


#Serializer for the Feedback model, used for sentiment analysis and saving data into database
class FeedbackSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(),write_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)
    class Meta:
        model = Feedback
        fields = [ 'customer', 'product', 'feedback_text', 'sentiment']
        read_only_fields = ['sentiment']  

    #creates feedback object in database
    def create(self, validated_data):
        validated_data['customer'] = validated_data.pop('customer')
        return super().create(validated_data)