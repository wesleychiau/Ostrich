# Generated by Django 2.0.5 on 2018-05-25 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ranges', '0002_auto_20180524_0709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rangestudents',
            name='rangeID',
        ),
        migrations.RemoveField(
            model_name='rangestudents',
            name='studentID',
        ),
        migrations.RemoveField(
            model_name='range',
            name='range_type',
        ),
        migrations.DeleteModel(
            name='RangeStudents',
        ),
    ]
