from tokenize import TokenError
from rest_framework import serializers
from django.contrib.auth import get_user_model,authenticate
from rest_framework_simplejwt.tokens import RefreshToken

User=get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields="all"
        read_only_fields=['created_at']

    def create(self, validated_data):
        user=User.objects.create_user(**validated_data)
        return user
    
class LoginSerializer(serializers.Serializer):
    username= serializers.CharField
    password= serializers.CharField(write_only=True)

    def validate(self, attrs):
        username= attrs.get('username')
        password= attrs.get('password')

        user= authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError('Username yoki password xato.')
        
        refresh= RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'username': user.username,
            'email': user.email,
        }
    
    
class RefreshSerializer(serializers.Serializer):
    refresh= serializers.CharField()

    def validate(self, attrs):
        refresh_token = attrs.get('refresh')

        try:
            token= RefreshToken(refresh_token)

            return {
                'access':str(token.access_token),
                'refresh': str(refresh_token)
            }
        
        except TokenError:
            raise serializers.ValidationError('Refresh token yaroqsiz')