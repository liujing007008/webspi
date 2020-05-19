from django.db import models


# Create your models here.


class Stock(models.Model):
    s_name = models.CharField(max_length=15)
    s_code = models.IntegerField(default=1)
    s_follow = models.IntegerField(default=0)