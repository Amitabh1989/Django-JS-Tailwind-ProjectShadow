# Generated by Django 4.2.2 on 2023-07-01 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testcase", "0005_alter_teststep_test_cases"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teststep",
            name="step",
            field=models.JSONField(null=True),
        ),
    ]