# Generated by Django 4.0.5 on 2022-06-08 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_remove_article_tags_article_scopes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(through='articles.SectionArticle', to='articles.section', verbose_name='Тэги'),
        ),
        migrations.AlterField(
            model_name='section',
            name='tag_name',
            field=models.CharField(max_length=30, verbose_name='Тэг'),
        ),
    ]
