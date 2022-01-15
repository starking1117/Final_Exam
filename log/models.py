from django.db import models

from equipment.models import equipment
from borrower.models import borrower

class Log(models.Model):
    number = models.ForeignKey(equipment, on_delete=models.CASCADE)
    person_who_borrow = models.ForeignKey(borrower, on_delete=models.CASCADE)
    checkout = models.DateTimeField('借用時間', auto_now_add=True)
    returned = models.DateTimeField('歸還時間', null=True)
