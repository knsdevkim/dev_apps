from rest_framework import serializers

from apps.models import *


class McpAPISerializer(serializers.ModelSerializer):
    class Meta:
        model  = Mcpmasterlist
        fields = '__all__'

class UserAPISerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = Users.objects.create(
            username   = validated_data['username'],
            email      = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name  = validated_data['last_name'],
            link_mcp   = validated_data['link_mcp'],
            user_type  = validated_data['user_type']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model  = Users
        fields = ('first_name', 'last_name', 'email', 'user_type', 'link_mcp', 'username', 'password')
