from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.models import User, Group
from django.db.models import Q
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.core.exceptions import ValidationError

from account.models import Customer


class CustomerSignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=200, write_only=True)
    email = serializers.EmailField(max_length=200)
    password = serializers.CharField(max_length=200, write_only=True, style={'input_type': 'password', 'placeholder': 'Password'} )
    confirm_password = serializers.CharField(max_length=200, write_only=True, style={'input_type': 'confirm_password', 'placeholder': 'Confirm_Password'} )

    def validate(self, attrs):
        if User.objects.filter(username=attrs["username"]).exists():
            raise serializers.ValidationError("A user with this userneme already exists")

        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError("Passwords do not match")

        try:
            password_validation.validate_password(attrs["password"])
        except ValidationError as e:
            raise serializers.ValidationError(str(e))

        return attrs


    def create_user(self, username, email, password):
        # this is a separate method so it's easy to override
        return User.objects.create_user(username=username, email=email, password=password)

    def save(self, *args, **kwargs):
        username = self.validated_data["username"]
        email = self.validated_data["email"]
        password = self.validated_data["password"]
        return self.create_user(username, email, password)

    class Meta:
        model = Customer
        fields = ['username', 'email', 'password', 'confirm_password']


class CustomerSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'phone_number', 'city', 'address', 'gender']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=12)
    password = serializers.CharField(max_length=30)

class CustomerLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length= 200, required=True)
    password = serializers.CharField(max_length=200, write_only=True)


    # def validate(self, attrs):
    #     username = attrs.get('username')
    #     password = attrs.get('password')
    #
    #     user = Customer.objects.filter(Q(username= username)).first()
    #
    #     if not user:
    #         raise serializers.ValidationError("User not found with given email/password")
    #
    #     if not user.check_password(password):
    #         raise serializers.ValidationError("Incorrect Password")
    #
    #     attrs['user'] = user
    #     return attrs

    class Meta:
        model = Customer
        fields = ['username', 'password']

