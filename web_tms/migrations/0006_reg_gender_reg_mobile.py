# Generated by Django 5.0.2 on 2024-03-12 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_tms', '0005_inqu'),
    ]

    operations = [
        migrations.AddField(
            model_name='reg',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='reg',
            name='mobile',
            field=models.BigIntegerField(null=True),
        ),
    ]