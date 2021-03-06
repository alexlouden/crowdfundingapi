# Generated by Django 3.0.8 on 2020-08-26 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_owner',
            field=models.BooleanField(default='False', verbose_name='owner status'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_supporter',
            field=models.BooleanField(default='False', verbose_name='supporter status'),
        ),
    ]
