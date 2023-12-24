from django.db import models
from ulid import ULID

# Create your models here.
def generate_ulid():
    return str(ULID())

# Create your models here.

class BaseModel(models.Model):
    id = models.CharField(max_length=128, default=generate_ulid, primary_key=True)

    class Meta:
        abstract = True
