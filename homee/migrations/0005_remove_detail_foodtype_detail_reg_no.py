# Generated by Django 4.1.2 on 2022-12-04 18:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homee', '0004_alter_detail_foodtype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='FoodType',
        ),
        migrations.AddField(
            model_name='detail',
            name='Reg_No',
            field=models.CharField(choices=[('CST/18/IFT/00125', 'CST/18/IFT/00125'), ('CST/18/IFT/00119', 'CST/18/IFT/00119'), ('CST/18/IFT/00118', 'CST/18/IFT/00118'), ('CST/18/IFT/00107', 'CST/18/IFT/00107'), ('CST/18/IFT/00101', 'CST/18/IFT/00101'), ('CST/18/IFT/00109', 'CST/18/IFT/00109')], default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
