# Generated by Django 4.2.2 on 2023-06-28 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testcase', '0002_testcase_teststep_test_case'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teststep',
            name='test_case',
        ),
        migrations.AddField(
            model_name='testcase',
            name='test_steps_list',
            field=models.ManyToManyField(to='testcase.teststep'),
        ),
        migrations.AddField(
            model_name='teststep',
            name='test_cases',
            field=models.ManyToManyField(related_name='test_steps', to='testcase.testcase'),
        ),
    ]