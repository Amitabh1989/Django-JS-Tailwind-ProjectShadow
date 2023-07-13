from django.db import models
from config.models import ConfigModel
# Create your models here.


class IOModel(models.Model):
    TOOL_CHOICES = [
        ('chaos', 'Chaos'),
        ('medusa', 'Medusa'),
    ]
    module_type = models.CharField(max_length=10, default='io', editable=False)
    tool = models.CharField(max_length=10, choices=TOOL_CHOICES)
    qd = models.IntegerField(default=1)
    raidlevel = models.CharField(max_length=12, choices=ConfigModel.RAIDS, default='R0')
    journal = models.CharField(max_length=100, default='--v compat')
    pattern = models.CharField(max_length=50, default='xoxo')
    random = models.IntegerField(choices=[(i, str(i)) for i in range(0, 101)], default='50')
    read = models.IntegerField(choices=[(i, str(i)) for i in range(0, 101)], default='1')
    runtime = models.CharField(max_length=10, default='-1')
    size = models.CharField(max_length=10, default='128')
    step_wait = models.CharField(max_length=15, default='30')
    completeio = models.BooleanField(default=False)
    expected_result = models.CharField(max_length=10, choices=[('fail', 'Fail'), ('pass', 'Pass')], default='pass')
    unaligned = models.BooleanField(default=False)
    verify = models.BooleanField(default=False)
    _use_count = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.tool} step submitted'

