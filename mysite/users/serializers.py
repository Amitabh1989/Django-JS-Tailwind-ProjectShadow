from rest_framework import serializers
from .models import User, UserManager

class UserModelSerializer(serializers.ModelSerializer):

    # This data is also displayed in browsable API page
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        # fields = ['id', 'name', 'email', 'tc', 'password', 'password2','is_admin']  # These are the data that we need to send for POST request
        fields = ['name', 'email', 'tc', 'password', 'password2']
        extra_kwargs = {
            'password':{
                'write_only': True
                }
        }
        print(f"User model serializer : Fields being displayed are : {fields}")
    
    def validate(self, attrs):
        if attrs.get('password') == attrs.get('password2'):
            return super().validate(attrs)
        raise serializers.ValidationError("Passwords does not match!!")  # this is seen as below
        """
        {
            "non_field_errors": [
                "Passwords does not match!!"
            ]
        }
        """

    def create(self, validated_data):
        print("IN serializer.py : Creating user")
        return User.objects.create_user(**validated_data)
        # return super().create(validated_data)


class UserLoginAuthSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255)
    class Meta:
        model = User
        fields = ["email", "password"]

class UserProfileSerializer(serializers.ModelSerializer):
    # email = serializers.CharField(max_length=255)
    class Meta:
        model = User
        fields = ["email", "id", "name"]