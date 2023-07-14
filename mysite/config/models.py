from django.db import models

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

    # testcase = models.
    # module_type = models.CharField(max_length=10, default='config', editable=False)
    # # raid = models.CharField(max_length=20, choices=RAID.choices, default=RAID.R0)
    # raid = models.CharField(max_length=20, choices=RAIDS)
    # vdcount = models.IntegerField(choices=NUM_VDS, default=1)
    # spans = models.IntegerField(choices=SPANS, default=1)
    # stripe = models.IntegerField(choices=STRIPE, default=128)
    # pdcount = models.IntegerField(choices=NUM_PDS, default=1)
    # size = models.IntegerField(default=10)
    # dtabcount = models.IntegerField(choices=NUM_DTABS, default=0)
    # hotspare = models.IntegerField(choices=NUM_DTABS, default=0)
    # init = models.CharField(max_length=10, choices=INIT, default='full')
    # readpolicy = models.CharField(max_length=6, choices=[("ra", "RA"), ("nora", "NORA")], default='ra')
    # writepolicy = models.CharField(max_length=6, choices=[("wb", "WB"), ("wt", "WT")], default='wt')
    # repeat = models.IntegerField(choices=NUM_VDS, default=1)
    
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
    _use_count =  models.IntegerField(default=1)

    def __str__(self) -> str:
        return f'<{self.raid.upper()} ({self.vdcount} VD) with {self.pdcount}PDs>'