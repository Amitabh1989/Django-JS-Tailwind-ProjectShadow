from django.db import models

# Create your models here.



class ConfigModel(models.Model):
    RAIDS = (
        ("R0", "R0"),
        ("R1", "R1"),
        ("R5", "R5"),
        ("R6", "R6"),
        ("JBODs", "JBODs"),
    )

    NUM_PDS = [(i, str(i)) for i in range(0, 241)]
    NUM_VDS = [(i, str(i)) for i in range(0, 32)]

    # testcase = models.
    raid = models.CharField(max_length=20, choices=RAIDS)
    num_pds = models.IntegerField(choices=NUM_PDS)
    size = models.CharField(max_length=10)
    num_vds = models.IntegerField(choices=NUM_VDS)

    def __str__(self) -> str:
        return f'{self.raid} ( {self.num_pds} VD ) with {self.num_pds} \
            submitted'