# Generated by Django 3.2.18 on 2023-05-19 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_rename_vote_movie_vote_average'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviereview',
            name='vote_average',
        ),
    ]
