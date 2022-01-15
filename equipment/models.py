from django.db import models
from type.models import type

class equipment(models.Model):
    number = models.CharField('設備編號',max_length=255)
    typo = models.ForeignKey(type, on_delete=models.CASCADE)
    property_number = models.CharField('財產編號',max_length=255)
    remark = models.CharField('備註',max_length=255,null=True,blank=True)
