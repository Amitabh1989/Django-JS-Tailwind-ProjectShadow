# Generated by Django 4.2.2 on 2023-07-11 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("config", "0004_alter_configmodel_dtabcount_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="configmodel",
            name="size",
            field=models.IntegerField(default=10),
        ),
    ]
