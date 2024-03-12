from rest_framework import serializers
from .models import Category

from django.utils.text import slugify

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
        read_only_fields = ['slug'] 

    def create(self, validated_data):
        name = validated_data.get('name')
        slug = slugify(name)  
        validated_data['slug'] = slug
        category = Category.objects.create(**validated_data)
        return category
