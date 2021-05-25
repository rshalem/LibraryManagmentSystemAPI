from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """custom attrs pass1 and pass2 for validation while registering"""
    password1 = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

    def validate(self, validated_data):
        if validated_data['password1'] != validated_data['password2']:
            raise serializers.ValidationError('Password didnt match')
        return validated_data

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password2']) #hashed
        user.save()
        return user