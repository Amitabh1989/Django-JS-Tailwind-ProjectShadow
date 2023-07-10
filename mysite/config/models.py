from django.db import models

# Create your models here.
class ConfigModel(models.Model):
    RAIDS = (
        ("R0", "R0"),
        ("R1", "R1"),
        ("R5", "R5"),
        ("R6", "R6"),
        ("R10", "R10"),
        ("R50", "R50"),
        ("R60", "R60"),
        ("JBODs", "JBODs"),
    )

    NUM_PDS = [(i, str(i)) for i in range(1, 241)]
    NUM_VDS = [(i, str(i)) for i in range(1, 32)]
    NUM_DTABS = [(i, str(i)) for i in range(0, 32)]
    SPANS = [(i, str(i)) for i in range(0, 8)]
    STRIPE = [(i, str(i)) for i in [64, 128, 256]]
    INIT = [("full", "FULL"), ("fast", "FAST"),
            ("no init", "No INIT"), ("autobgi", "AutoBGI")]

    # testcase = models.
    module_type = models.CharField(max_length=15, default='config', editable=False)
    raid = models.CharField(max_length=20, choices=RAIDS)
    vdcount = models.IntegerField(choices=NUM_VDS)
    spans = models.IntegerField(choices=SPANS)
    stripe = models.IntegerField(choices=STRIPE)
    pdcount = models.IntegerField(choices=NUM_PDS)
    size = models.CharField(max_length=10)
    dtabcount = models.IntegerField(choices=NUM_DTABS)
    hotspare = models.IntegerField(choices=NUM_DTABS)
    init = models.CharField(max_length=10, choices=INIT)
    readpolicy = models.CharField(max_length=6, choices=[("ra", "RA"), ("nora", "NORA")])
    writepolicy = models.CharField(max_length=6, choices=[("wb", "WB"), ("wt", "WT")])
    repeat = models.IntegerField(choices=NUM_VDS)
    
    def __str__(self) -> str:
        return f'{self.raid} ({self.vdcount} VD) with {self.pdcount}PDs submitted'