# Generated by Django 2.2.6 on 2019-10-26 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_check', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurancecompany',
            name='polis_ltd_date_end',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='services',
            name='polis_ltd_outservice',
            field=models.TextField(max_length=200),
        ),
    ]
