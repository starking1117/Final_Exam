# Generated by Django 3.2.9 on 2022-01-15 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0003_rename_typo_equipment_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipment',
            old_name='type',
            new_name='typo',
        ),
    ]
