# Generated by Django 4.0.5 on 2022-06-08 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_article_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tag',
            new_name='tags',
        ),
    ]
