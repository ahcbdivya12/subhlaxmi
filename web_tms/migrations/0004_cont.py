# Generated by Django 5.0.2 on 2024-03-08 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_tms', '0003_god'),
    ]

    operations = [
        migrations.CreateModel(
            name='cont',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('subject', models.CharField(max_length=40)),
                ('message', models.CharField(max_length=400)),
            ],
        ),
    ]
