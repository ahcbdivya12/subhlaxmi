# Generated by Django 5.0.2 on 2024-03-08 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_tms', '0004_cont'),
    ]

    operations = [
        migrations.CreateModel(
            name='inqu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('lname', models.CharField(max_length=40)),
                ('mobile', models.BigIntegerField()),
                ('email', models.CharField(max_length=40)),
                ('subject', models.CharField(max_length=40)),
                ('message', models.CharField(max_length=400)),
            ],
        ),
    ]