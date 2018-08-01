# Generated by Django 2.0.7 on 2018-07-31 02:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SDL', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SDLComment',
            fields=[
                ('commentid', models.AutoField(db_column='commentID', primary_key=True, serialize=False)),
                ('comment', models.CharField(db_column='comment', max_length=255, null=True)),
                ('dateposted', models.DateField(db_column='datePosted', null=True)),
                ('timeposted', models.TimeField(db_column='timePosted', null=True)),
                ('commenter', models.ForeignKey(db_column='commenter', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'SDLComments',
                'db_table': 'SDLComment',
            },
        ),
        migrations.AlterModelOptions(
            name='sdlpost',
            options={'verbose_name_plural': 'SDLPosts'},
        ),
        migrations.RenameField(
            model_name='sdlpost',
            old_name='postID',
            new_name='postid',
        ),
        migrations.RemoveField(
            model_name='sdlpost',
            name='isdisabled',
        ),
        migrations.AddField(
            model_name='sdlpost',
            name='createdby',
            field=models.ForeignKey(db_column='createdby', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='SDLcreatedby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sdlpost',
            name='postactive',
            field=models.BooleanField(db_column='postActive', default=False),
        ),
        migrations.AddField(
            model_name='sdlcomment',
            name='postid',
            field=models.ForeignKey(db_column='postid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='SDL.SDLPost'),
        ),
    ]
