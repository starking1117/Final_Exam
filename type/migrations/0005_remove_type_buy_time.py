# Generated by Django 3.2.9 on 2022-01-15 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('type', '0004_alter_type_buy_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type',
            name='buy_time',
        ),
    ]
