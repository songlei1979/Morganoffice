# Generated by Django 3.0.8 on 2020-08-03 00:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morgan', '0003_auto_20200803_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(1)]),
        ),
    ]
