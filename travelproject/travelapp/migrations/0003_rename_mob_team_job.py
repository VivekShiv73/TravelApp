# Generated by Django 4.2.6 on 2023-11-02 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team.css',
            old_name='mob',
            new_name='job',
        ),
    ]
