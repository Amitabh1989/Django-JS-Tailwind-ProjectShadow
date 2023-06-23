from django.db import models

# Create your models here.


class TestCase(models.Model):
    cqid = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=2000)

    def __str__(self) -> str:
        return self.title

class TestStep(models.Model):
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE, related_name='test_steps')
    step = models.CharField(max_length=10000)

    def __str__(self):
        return self.step