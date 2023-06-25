# Generated by Django 4.2.1 on 2023-06-22 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("testcase", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TestCase",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cqid", models.CharField(max_length=20)),
                ("title", models.CharField(max_length=100)),
                ("summary", models.TextField(max_length=2000)),
            ],
        ),
        migrations.AddField(
            model_name="teststep",
            name="test_case",
            field=models.ForeignKey(
                default=123,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="test_steps",
                to="testcase.testcase",
            ),
            preserve_default=False,
        ),
    ]