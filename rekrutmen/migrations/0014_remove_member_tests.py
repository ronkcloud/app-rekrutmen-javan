# Generated by Django 3.2.4 on 2021-07-02 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rekrutmen', '0013_joblist_tests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='tests',
        ),
    ]
