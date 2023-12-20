from django.db import models
from ulid import ULID

# Create your models here.
def generate_ulid():
    return str(ULID())


class GrinderBrand(models.Model):
    id = models.CharField(max_length=128, default=generate_ulid, primary_key=True)
    name = models.CharField(max_length=128, null=False, default="")

    def __str__(self):
        return self.name

class Grinder(models.Model):
    id = models.CharField(max_length=128, default=generate_ulid, primary_key=True)
    model = models.CharField(max_length=255, null=False, default="")
    brand = models.ForeignKey(to=GrinderBrand, on_delete=models.CASCADE, related_name="grinder_brand")

    def __str__(self):
        return "{} {}".format(self.brand, self.model)

