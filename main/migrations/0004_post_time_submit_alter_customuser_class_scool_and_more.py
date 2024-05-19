# Generated by Django 5.0.6 on 2024-05-19 10:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_status_application_application_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='time_submit',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='class_scool',
            field=models.CharField(choices=[('5А', '5А'), ('5Б', '5Б'), ('5В', '5В'), ('5Г', '5Г'), ('6А', '6А'), ('6Б', '6Б'), ('6В', '6В'), ('6Г', '6Г'), ('7А', '7А'), ('7Б', '7Б'), ('7В', '7В'), ('7Г', '7Г'), ('8А', '8А'), ('8Б', '8Б'), ('8В', '8В'), ('8Г', '8Г'), ('9А', '9А'), ('9Б', '9Б'), ('9В', '9В'), ('9Г', '9Г'), ('10А', '10А'), ('10Б', '10Б'), ('10В', '10В'), ('10Г', '10Г'), ('11А', '11А'), ('11Б', '11Б'), ('11В', '11В'), ('11Г', '11Г')], max_length=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_event',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='time_submit',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]