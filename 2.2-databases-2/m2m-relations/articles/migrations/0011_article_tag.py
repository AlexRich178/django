# Generated by Django 4.0.5 on 2022-06-08 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_remove_article_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(related_name='tags', through='articles.SectionArticle', to='articles.section', verbose_name='Тэги'),
        ),
    ]
