# Generated by Django 4.1.5 on 2023-01-15 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_scope_article_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(verbose_name='Основной'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.tag', verbose_name='Раздел'),
        ),
    ]
