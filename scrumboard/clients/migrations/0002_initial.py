# Generated by Django 4.2.6 on 2023-10-23 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='contact_person',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.contact'),
        ),
    ]
