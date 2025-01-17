from rest_framework import serializers
from website.models import Customer,Product, Feedback

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']  



class FeedbackSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(),write_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)
    class Meta:
        model = Feedback
        fields = [ 'customer', 'product', 'feedback_text', 'sentiment']
        read_only_fields = ['sentiment']  

    def create(self, validated_data):
        validated_data['customer'] = validated_data.pop('customer')
        return super().create(validated_data)