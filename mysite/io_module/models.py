from django.db import models
from myapp.models import ConfigModel
# Create your models here.


class IOModule(models.Model):
    TOOL_CHOICES = [
        ('chaos', 'Chaos'),
        ('medusa', 'Medusa'),
    ]
    module_type = models.CharField(max_length=10, default='io', editable=False)
    tool = models.CharField(max_length=10, choices=TOOL_CHOICES)
    qd = models.IntegerField()
    raidlevel = models.CharField(max_length=12, choices=ConfigModel.RAIDS)
    journal = models.CharField(max_length=100)
    pattern = models.CharField(max_length=50)
    random = models.IntegerField(choices=[(i, str(i)) for i in range(0, 101)])
    read = models.IntegerField(choices=[(i, str(i)) for i in range(0, 101)])
    runtime = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    step_wait = models.CharField(max_length=15)
    completeio = models.BooleanField(default=False)
    expected_result = models.CharField(max_length=10, choices=[('fail', 'Fail'), ('pass', 'Pass')])
    unaligned = models.BooleanField(default=False)
    verify = models.BooleanField(default=False)

    def __str__(self):
        return self.journal

