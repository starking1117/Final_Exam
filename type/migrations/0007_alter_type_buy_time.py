# Generated by Django 3.2.9 on 2022-01-15 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('type', '0006_type_buy_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='buy_time',
            field=models.DateTimeField(),
        ),
    ]
