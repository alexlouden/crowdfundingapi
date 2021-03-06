# Generated by Django 3.0.8 on 2020-09-03 04:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0009_auto_20200828_0239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='shelter',
        ),
        migrations.AddField(
            model_name='shelter',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='species',
            field=models.ManyToManyField(related_name='projects', related_query_name='projects', to='projects.PetTag'),
        ),
        migrations.AlterField(
            model_name='shelter',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='shelter', to=settings.AUTH_USER_MODEL),
        ),
    ]
