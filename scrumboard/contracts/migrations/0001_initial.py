# Generated by Django 4.2.6 on 2023-10-23 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default='', max_length=10)),
                ('contracting_date', models.DateField(default=None, null=True)),
                ('contracting_kind', models.CharField(choices=[('estimation', 'Kostenschätzung'), ('calculation', 'Kostenberechnung'), ('tender', 'Ausschreibung')], default='', max_length=20)),
                ('order_value', models.IntegerField(default='')),
                ('date_start', models.DateField(default=None, null=True)),
                ('date_end', models.DateField(default=None, null=True)),
                ('precessing_time', models.DurationField(default='')),
                ('client', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.client')),
            ],
        ),
    ]