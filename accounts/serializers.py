from rest_framework import serializers
from django.contrib.auth.models import User

# User Serializer
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

# Register Serializer


class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email',
                  'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}, }

    # def create(self, validated_data):
    #     user = User.objects.create_user(
    #         validated_data['username'], validated_data['email'], validated_data['password'])

    #     return user

    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data.get('password'))
        return super(RegisterSerializer, self).create(validated_data)
