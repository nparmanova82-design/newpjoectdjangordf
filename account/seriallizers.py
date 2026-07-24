from rest_framework import serializers
from django.contrib.auth import get_user_model,authenticate

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
    email=serializers.EmailField()
    password=serializers.CharField(write_only=True)

    def validate(self,attrs):
        user=authenticate(
            email=attrs["username"],
            password=attrs["password"],
        )

        if not user:
            raise serializers.ValidationError("parol yoki email xato") 
        attrs["user"]=user
        return attrs