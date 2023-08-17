from django.db import models
from config.models import ConfigModel
from users.models import User
# Create your models here.


class IOModel(models.Model):
    TOOL_CHOICES = [
        ('chaos', 'Chaos'),
        ('medusa', 'Medusa'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    
    def save(self, *args, **kwargs):
        print(f"Kwargs received in IO save is : {kwargs}")
        # Request received in Config save is : {'_state': <django.db.models.base.ModelState object at 0x7fdf5394d810>,
        # 'id': 1, 'user_id': 1, 'module_type': 'config', 'raid': 'r0', 'vdcount': 1,
        # 'spans': 0, 'stripe': 64, 'pdcount': 1, 'size': 12, 'dtabcount': 0, 'hotspare': 0,
        # 'init': 'full', 'readpolicy': 'ra', 'writepolicy': 'wb', 'repeat': 1, '_use_count': 2}
        
        # Need to do 2 things here.
        # 1. Check if record exists. If so, just update the use count and updated_time
        # 2. If record does not exist, save new record and update use count and time created

        # Check if record exists
        
        self._use_count += 1
        super().save(*args, **kwargs)

        print(f"Request received in Config save is : {self.__dict__}")


