from rest_framework import serializers
from .models import Authors

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Authors
        fields = '__all__'
    
    def validate(self, data):
        if len(data['author_name']) and len(data['bio']) <=2:
            raise serializers.ValidationError('Characters cannot be less than 2')
        return data

    def create(self, validated_data):
        author_name = validated_data.get('author_name','')
        bio = validated_data.get('bio','')
        if not author_name and bio:
            raise serializers.ValidationError('Invalid author details')
        return Authors.objects.create(author_name=author_name,bio=bio)