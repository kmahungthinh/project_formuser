# Generated by Django 4.1 on 2022-09-18 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='diachi',
            field=models.CharField(default=-1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='sodienthoai',
            field=models.CharField(default=-1, max_length=12),
            preserve_default=False,
        ),
    ]
