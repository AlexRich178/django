# Generated by Django 4.0.5 on 2022-06-28 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0007_alter_measurement_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='date',
            field=models.DateField(),
        ),
    ]
