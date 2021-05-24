from rest_framework import serializers

from .models import Categories

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
    
    def validate(self, data):
        if not data['category_name']:
            raise serializers.ValidationError('Category title cant be empty')
        if Categories.objects.filter(category_name__iexact=data['category_name']).exists():
            raise serializers.ValidationError('Category with title {} exists'.format(data['category_name']))
        return data