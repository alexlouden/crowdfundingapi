# Generated by Django 3.0.8 on 2020-08-26 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20200826_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pettag',
            name='petspecies',
            field=models.CharField(max_length=200),
        ),
    ]
