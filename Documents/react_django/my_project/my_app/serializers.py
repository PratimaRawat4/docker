from rest_framework import serializers
from .models import Product



class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Product
        fields = '__all__'


    def get_image(self, obj):
        request = self.context.get('request')  # Access the request from the serializer context
        if obj.image:
            return request.build_absolute_uri(obj.image.url)  # Construct full URL
        return None  # Return `None` if no image is provided

        
