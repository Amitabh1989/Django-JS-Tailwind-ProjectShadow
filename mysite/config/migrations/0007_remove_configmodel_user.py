# Generated by Django 4.2.2 on 2023-08-12 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("config", "0006_alter_configmodel_module_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="configmodel",
            name="user",
        ),
    ]