# Generated by Django 3.2.9 on 2022-01-15 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('type', '0002_auto_20220115_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='detailed',
            field=models.TextField(max_length=25, verbose_name='詳細規格'),
        ),
        migrations.AlterField(
            model_name='type',
            name='type',
            field=models.CharField(max_length=25, verbose_name='型號'),
        ),
    ]
