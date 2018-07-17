# Generated by Django 2.0.6 on 2018-07-16 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranges', '0007_auto_20180716_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='range',
            name='attempts',
            field=models.PositiveIntegerField(db_column='attempts', default=0),
        ),
        migrations.AddField(
            model_name='range',
            name='rangeinfo',
            field=models.TextField(blank=True, db_column='rangeInfo', null=True),
        ),
    ]