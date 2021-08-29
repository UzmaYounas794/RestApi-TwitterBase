from rest_framework import serializers
from tweet.models import Tweet
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class TweetSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Tweet.objects.create(**validated_data)

    class Meta:
        model = Tweet
        fields = ["id", "user", "body", "created_at", "updated_at"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(email=validated_data["email"], username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        Token.objects.create(user=user)
        return user
