# Generated by Django 3.0.8 on 2020-08-28 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20200827_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelter',
            name='address',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shelter',
            name='charityregister',
            field=models.IntegerField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
