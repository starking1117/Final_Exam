from django.db import models

class type(models.Model):

    ST_OPTIONS = [
    (0, '使用中'),
    (1, '已報廢除帳'),
    ]

    type = models.CharField('型號', max_length=25)
    buy_time = models.DateTimeField('購買時間', auto_now_add=True)
    detailed = models.TextField('詳細規格', max_length=25)
    status = models.IntegerField(
              '狀態', 
              default=0, 
              choices=ST_OPTIONS
           )