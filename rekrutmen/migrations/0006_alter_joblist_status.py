# Generated by Django 3.2.4 on 2021-06-26 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekrutmen', '0005_joblist_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblist',
            name='status',
            field=models.CharField(choices=[('review', 'proses review'), ('diterima', 'diterima'), ('ditolak', 'ditolak')], default='review', max_length=10, null=True),
        ),
    ]