from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import *

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True,)
    category = CategorySerializer()
    class Meta:
        model= Post
        fields = ('title','text','slug','feature_image','thumbnail_image', 'published_date','category','tags')

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username','phone_number','email','state','country','city','password')

class CommentSerializer(serializers.ModelSerializer):
    # post = PostSerializer()
    class Meta:
        model = Comment
        fields = ('post','parent','email','name','text')

# class SignupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username','phone_number','email','state','country','city','password','user_profile_image')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','phone_number','email','state','country','city','password','user_profile_image']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")

