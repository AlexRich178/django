# Generated by Django 4.0.5 on 2022-06-08 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0016_alter_section_primary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='primary',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='sectionarticle',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_of', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='sectionarticle',
            name='tags',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag_of', to='articles.section'),
        ),
    ]
