# Generated by Django 5.0.2 on 2024-03-05 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inHive', '0002_hive_queenbee_membership_hive_queenbee_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='hiveEnDate',
            new_name='taskEnDate',
        ),
    ]
