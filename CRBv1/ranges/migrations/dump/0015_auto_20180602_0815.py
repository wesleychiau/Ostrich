# Generated by Django 2.0.5 on 2018-06-02 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ranges', '0014_auto_20180602_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='range',
            name='username',
            field=models.ForeignKey(db_column='createdby', default='super', on_delete=django.db.models.deletion.DO_NOTHING, related_name='CBR', to=settings.AUTH_USER_MODEL),
        ),
    ]
