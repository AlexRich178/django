# Generated by Django 4.0.5 on 2022-06-08 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0018_alter_section_primary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='primary',
            new_name='is_main',
        ),
    ]
