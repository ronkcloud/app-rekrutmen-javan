# Generated by Django 3.2.4 on 2021-06-26 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekrutmen', '0004_joblist'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblist',
            name='status',
            field=models.CharField(choices=[('review', 'review'), ('diterima', 'diterima'), ('ditolak', 'ditolak')], default='review', max_length=10, null=True),
        ),
    ]
