# Generated by Django 4.2.6 on 2023-10-23 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contracts', '0001_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='contractor',
            field=models.ForeignKey(default='', limit_choices_to={'designation': 'Geschäftsführung'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contractor', to='employees.employee'),
        ),
    ]
