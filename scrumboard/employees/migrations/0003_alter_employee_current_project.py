# Generated by Django 4.2.6 on 2023-10-23 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
        ('employees', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='current_project',
            field=models.ManyToManyField(blank=True, default='', null=True, to='project.project'),
        ),
    ]
