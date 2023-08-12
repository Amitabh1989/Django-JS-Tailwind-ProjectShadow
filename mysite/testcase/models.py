from django.db import models
import json
from users.models import User

# Create your models here.


# class TestCase(models.Model):
#     cqid = models.CharField(max_length=20)
#     title = models.CharField(max_length=100)
#     summary = models.TextField(max_length=2000)
#     # test_steps_list = models.ManyToManyField('TestStep')

#     def __str__(self) -> str:
#         return self.title

# class TestStep(models.Model):
#     test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE, related_name='test_steps')
#     step = models.CharField(max_length=10000)

#     def __str__(self):
#         return self.step

class TestCase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cqid = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=2000)
    test_steps_list = models.ManyToManyField("TestStep")  # using reverse relation ship name : test_steps_list
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.title

class TestStep(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_cases = models.ManyToManyField(TestCase, related_name='teststep')
    step = models.JSONField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    # use_count = models.IntegerField(default=0)

    def __str__(self):
        return json.dumps(self.step) if self.step else ""