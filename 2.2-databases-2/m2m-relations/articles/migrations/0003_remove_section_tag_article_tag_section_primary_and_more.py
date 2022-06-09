# Generated by Django 4.0.5 on 2022-06-08 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_section'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='tag',
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(related_name='tags', to='articles.section'),
        ),
        migrations.AddField(
            model_name='section',
            name='primary',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='section',
            name='tag_name',
            field=models.CharField(default='TAG', max_length=30, verbose_name='Тэг'),
        ),
        migrations.CreateModel(
            name='SectionArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
                ('tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.section')),
            ],
        ),
    ]