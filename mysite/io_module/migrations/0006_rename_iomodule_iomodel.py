# Generated by Django 4.2.2 on 2023-07-11 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("io_module", "0005_alter_iomodule_expected_result_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="IOModule",
            new_name="IOModel",
        ),
    ]
