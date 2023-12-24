from django.db import models
from ulid import ULID

from base.models import BaseModel


def generate_ulid():
    return str(ULID())
#
# # Create your models here.
#
class Dripper(BaseModel):
    model = models.CharField(max_length=128, null=False)
    brand = models.CharField(max_length=128, null=False)

    class Meta:
        db_table = "dripper"
        
    def __str__(self):
        return "{} {}".format(self.brand, self.model)

class Scale(BaseModel):
    model = models.CharField(max_length=128, null=False)
    brand = models.CharField(max_length=128, null=False)

    class Meta:
        db_table = "scale"

    def __str__(self):
        return "{} {}".format(self.brand, self.model)
    

class EspressoMachine(BaseModel):
    model = models.CharField(max_length=128, null=False)
    brand = models.CharField(max_length=128, null=False)

    class Meta:
        db_table = "espresso_machine"

    def __str__(self):
        return "{} {}".format(self.brand, self.model)


