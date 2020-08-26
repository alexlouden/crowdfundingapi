from rest_framework import serializers
from .models import CustomUser, SupporterProfile, OwnerProfile

class SupporterSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    bio = serializers.CharField(max_length=200, source='supporter.bio')

    def create(self, validated_data):
        print(validated_data)
        supporter_data = validated_data.pop('supporter')
        newuser = CustomUser.objects.create(**validated_data)
        newsupporter = SupporterProfile.objects.create(user=newuser, **supporter_data)
        return newuser

    def update(self, user, validated_data):
        print(user)
        print(validated_data)
        user.username = validated_data.get('username', user.username)
        user.email = validated_data.get('email', user.email)
        user.save()
        print(user)
        print(user.supporter)
        user.supporter.bio = validated_data.get('bio', user.supporter.bio)
        user.supporter.save()
        return user

class OwnerSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    shelterid = serializers.CharField(max_length=200, source='owner.shelterid')

    def create(self, validated_data):
        print(validated_data)
        owner_data = validated_data.pop('owner')
        newuser = CustomUser.objects.create(**validated_data)
        newowner = OwnerProfile.objects.create(user=newuser, **owner_data)
        return newuser

    def update(self, user, validated_data):
        user.username = validated_data.get('username', user.username)
        user.email = validated_data.get('email', user.email)
        user.save()
        user.owner.shelterid = validated_data.get('shelterid', user.owner.bio)
        user.owner.save()
        return user