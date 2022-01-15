from django.db import models

# 借用人資料
class borrower(models.Model):

    ID_OPTIONS = [
    (0, '正式教師'),
    (1, '行政人員'),
    (2, '代理教師'),
    (3, '兼任教師'),
    ]

    LEVEL_OPTIONS = [
    (0, '國中部'),
    (1, '高中部'),
    ]

    ST_OPTIONS = [
    (0, '在職'),
    (1, '已離職'),
    ]
    realname = models.CharField('姓名', max_length=32)
    identity = models.IntegerField(
              '身分', 
              default=0, 
              choices=ID_OPTIONS
           )
    level = models.IntegerField(
              '國/高中部', 
              default=0, 
              choices=LEVEL_OPTIONS
           )
    teaching = models.CharField('科目', max_length=30)
    administration = models.CharField('職稱', max_length=30)
    tel = models.CharField('聯絡電話', max_length=255)
    email = models.EmailField('電子信箱')
    status = models.IntegerField(
              '狀態', 
              default=0, 
              choices=ST_OPTIONS
           )

    def __str__(self):
        return "{} / {} / {}".format(
            self.realname, 
            self.email, 
            self.tel
        )