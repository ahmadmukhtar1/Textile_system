# Generated by Django 4.1.2 on 2022-10-23 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='FoodType',
        ),
    ]