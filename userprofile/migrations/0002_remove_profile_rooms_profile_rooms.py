# Generated by Django 5.1 on 2024-08-24 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='rooms',
        ),
        migrations.AddField(
            model_name='profile',
            name='rooms',
            field=models.ManyToManyField(related_name='profiles', to='room.room'),
        ),
    ]
