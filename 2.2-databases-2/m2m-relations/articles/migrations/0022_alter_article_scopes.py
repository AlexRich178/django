# Generated by Django 4.0.5 on 2022-06-08 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0021_remove_section_is_main_remove_section_some_field_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(related_name='test', through='articles.SectionArticle', to='articles.section', verbose_name='Тэги'),
        ),
    ]
