# Generated by Django 4.2.1 on 2023-06-17 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_watchlist_avg_reting_watchlist_number_ratings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='avg_reting',
            new_name='avg_rating',
        ),
    ]