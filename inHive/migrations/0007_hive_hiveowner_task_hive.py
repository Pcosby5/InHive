# Generated by Django 5.0.2 on 2024-03-08 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inHive', '0006_remove_hive_queenbee_rename_user_membership_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hive',
            name='HiveOwner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inHive.user'),
        ),
        migrations.AddField(
            model_name='task',
            name='hive',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inHive.hive'),
            preserve_default=False,
        ),
    ]
