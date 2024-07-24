from django.db import models

# Create your models here.
class URL(models.Model):
    long_url=models.URLField()
    short_code=models.CharField(max_length=5,unique=True)

def str(self):
    return f'{short_code}:{long_URL}'
