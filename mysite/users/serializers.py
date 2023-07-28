from rest_framework import serializers
from .models import User, UserManager
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from .utils import Util 

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


class UserChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, style={"input_type": "password"}, write_only=True)
    password2 = serializers.CharField(max_length=255, style={"input_type": "password"}, write_only=True)
    class Meta:
        model = User
        fields = ["password", "password2"]

    def validate(self, attrs):
        print(f"Attributes are : {attrs}")
        password = attrs.get("password")
        password2 = attrs.pop('password2')
        if password != password2:
            raise serializers.ValidationError("Passwords do not match")
        user = self.context.get("user")
        print(f"User is : {user}")
        print(f"Returning attrs : {attrs}")
        return attrs

    def update(self, instance, validated_data):
        password = validated_data.get("password")
        print(f"Instance is : {instance}")
        
        if password:
            instance.set_password(password)
            instance.save()
            print(f"Instance saved : {instance}")

        return instance


class SendResetPasswordEmailSerializer(serializers.ModelSerializer):
        
    """
    Q : Why the email send url is not reset-password and is only reset?
    A : 
        In Django, when defining URL patterns, you can choose any term or string
        you prefer for the URL pattern. The term you choose in the URL pattern is
        used to match the corresponding part of the URL. The term is not required 
        to match the exact string used in the URL itself.

        In your case,
        the URL pattern is defined as path('reset-password/<uid>/<token>/',
        UserPasswordResetView.as_view(), name='reset-password').
        Here, reset-password is the term chosen for the URL pattern.
        It is a placeholder that will match any string that appears in the
        corresponding part of the URL.

        When a request is
        made to 'http://localhost:3000/api/user/reset/'+uid+'/'+token, Django's URL
        resolver will examine the URL patterns defined in your Django project's URL
        configuration. It will compare the different parts of the URL against the
        defined URL patterns to find a match.

        In this case, Django will match the URL against the reset-password URL
        pattern because the structure and format of the URL match. The dynamic
        parameters <uid> and <token> will be extracted from the URL and passed as
        arguments to the UserPasswordResetView.

        To summarize, the term used in the URL pattern (reset-password) does not
        need to match the exact string used in the URL you are constructing
        ('http://localhost:3000/api/user/reset/'+uid+'/'+token). Django's URL
        resolver uses the URL pattern to determine the appropriate view to handle
        the request based on the structure and format of the URL.
    """
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ["email"]

    def validate(self, attrs):
        print(f"Attributes are : {attrs}")
        email = attrs.get("email")
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("EMail not found. User not authenticated")    
        print("Email validated")
        user = User.objects.get(email=email)
        uid = urlsafe_base64_encode(force_bytes(user.id))
        token = PasswordResetTokenGenerator().make_token(user)
        url_link = 'http://localhost:3000/auth/reset/' + uid + "/" + token
        print(f"Url Link is : {url_link}")

        # Send email with reset password link
        data = {
            "subject": "Password Reset Link",
            "body": f"Click on this link to reset password : {url_link}",
            "to_email": user.email
        }
        Util.send_mail(data)
        return attrs


class ValidateResetPasswordSerializer(serializers.Serializer):  
    password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
    password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
    class Meta:
        fields = ['password', 'password2']

    def validate(self, attrs):
        # try:
        print("I have been called ValidateResetPasswordSerializer")
        password = attrs.get("password")
        password2 = attrs.pop("password2")
        uid = self.context.get("uid")
        token = self.context.get("token")
        if password != password2:
            raise serializers.ValidationError("Passwords dont match!")
        print("Password is valid")
        uid = smart_str(urlsafe_base64_decode(uid))
        user = User.objects.get(id=uid)
        
        if not user:
            raise serializers.ValidationError("User not found")
        
        if not PasswordResetTokenGenerator().check_token(user, token):
            raise serializers.ValidationError("Invalid token")
        print("User and token validated !")
        attrs["user"] = user
        print(f"Attrs : {attrs}")
        return attrs
        # except DjangoUnicodeDecodeError as indentifier:
        #     PasswordResetTokenGenerator().check_token(user, token)
        #     raise serializers.ValidationError("Token is not valid")

    def update(self, instance, validated_data):
        password = validated_data.get("password")
        print(f"Instance is : {instance}")
        
        if password:
            instance.set_password(password)
            instance.save()
            print(f"Instance saved : {instance}")

        return instance
