# Generated by Django 4.0.5 on 2022-06-08 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_section_tag_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name': 'Раздел', 'verbose_name_plural': 'Разделы'},
        ),
    ]
