# Generated by Django 3.0.8 on 2020-08-26 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200822_0132'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('petspecies', models.TextField()),
                ('Projectname', models.ManyToManyField(related_name='pets', related_query_name='pet', to='projects.Project')),
            ],
        ),
    ]
