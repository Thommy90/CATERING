from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class UserRegistratrionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "phone_number",
            "first_name",
            "last_name",
            "password",
        ]

    def validate(self, attrs: dict) -> dict:
        """Change the password for its hash to make token validation available"""

        attrs["password"] = make_password(attrs["password"])

        return attrs


class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "phone_number", "first_name", "last_name", "role"]


class UserActivationSerializer(serializers.Serializer):
    key = serializers.UUIDField()

from django.contrib.auth import get_user_model

User = get_user_model()

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {"detail": "Invalid email or password. Please try again."}
            )

        if not user.check_password(password):
            raise serializers.ValidationError(
                {"detail": "Invalid email or password. Please try again."}
            )

        if not user.is_active:
            raise serializers.ValidationError(
                {"detail": "Account not active. Please check your email to activate your account."}
            )

        return super().validate(attrs)