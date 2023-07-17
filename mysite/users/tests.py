from django.test import TestCase
from .models import User
# Create your tests here.

class UserProfileTest(TestCase):

    def test_user_profile_created(self):
        user = User(
            email= "root@example.com",
            password= "example",
            name="example",
            tc=True
        )
        user.save()
        print(f"User is : {user}")
        print(f"User is : {user.__dict__}")
        self.assertTrue(
            hasattr(user, 'userprofile')
        )