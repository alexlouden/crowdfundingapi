from rest_framework import serializers
from .models import CustomUser, Profile


class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    bio = serializers.CharField(max_length=200, source='profile.bio')
    is_supporter = serializers.BooleanField(read_only=True)
    is_owner = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        profile_data = validated_data.pop('profile')
        new_user = CustomUser.objects.create(**validated_data)
        # update user profile data
        Profile.objects.filter(user=new_user).update(**profile_data)
        # refresh the user
        new_user.refresh_from_db()
        return new_user

    def update(self, user, validated_data):
        print(user)
        print(validated_data)
        user.username = validated_data.get('username', user.username)
        user.email = validated_data.get('email', user.email)
        profile_data = validated_data.get('profile')
        if profile_data:
            user.profile.bio = profile_data.get('bio', user.profile.bio)
        user.save()
        return user
