from django.db import models
from users.models import User

# Create your models here.
class ConfigModel(models.Model):
#     class RAID(models.TextChoices):
#         R0 = "1", "R0"
#         R1 = "2", "R1"
#         R5 = "3", "R5"
#         R6 = "4", "R6"
#         R10 = "5", "R10"
#         R50 = "6", "R50"
#         R60 = "7", "R60"
#         JBOD = "8", "JBOD"
    RAIDS = [
        ("r0", "R0"),
        ("r1", "R1"),
        ("r5", "R5"),
        ("r6", "R6"),
        ("r10", "R10"),
        ("r50", "R50"),
        ("r60", "R60"),
        ("jbod", "JBOD"),
    ]

    NUM_PDS = [(i, str(i)) for i in range(1, 241)]
    NUM_VDS = [(i, str(i)) for i in range(1, 32)]
    NUM_DTABS = [(i, str(i)) for i in range(0, 32)]
    SPANS = [(i, str(i)) for i in range(0, 8)]
    STRIPE = [(i, str(i)) for i in [64, 128, 256]]
    INIT = [("full", "FULL"), ("fast", "FAST"),
            ("no init", "No INIT"), ("autobgi", "AutoBGI")]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    module_type = models.CharField(max_length=10, default='config', editable=False)
    # raid = models.CharField(max_length=20, choices=RAID.choices, default=RAID.R0)
    raid = models.CharField(max_length=20, choices=RAIDS)
    vdcount = models.IntegerField(choices=NUM_VDS)
    spans = models.IntegerField(choices=SPANS)
    stripe = models.IntegerField(choices=STRIPE)
    pdcount = models.IntegerField(choices=NUM_PDS)
    size = models.IntegerField()
    dtabcount = models.IntegerField(choices=NUM_DTABS)
    hotspare = models.IntegerField(choices=NUM_DTABS)
    init = models.CharField(max_length=10, choices=INIT)
    readpolicy = models.CharField(max_length=6, choices=[("ra", "RA"), ("nora", "NORA")], default='ra')
    writepolicy = models.CharField(max_length=6, choices=[("wb", "WB"), ("wt", "WT")], default='wt')
    repeat = models.IntegerField(choices=NUM_VDS)
    _use_count =  models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'<{self.raid.upper()} ({self.vdcount} VD) with {self.pdcount}PDs>'


    def save(self, *args, **kwargs):
        print(f"Kwargs received in Config save is : {kwargs}")
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
