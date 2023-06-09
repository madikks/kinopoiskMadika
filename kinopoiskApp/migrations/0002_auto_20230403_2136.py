# Generated by Django 3.1 on 2023-04-03 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinopoiskApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='isRecommended',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Рекомендуется'),
        ),
        migrations.AddField(
            model_name='movie',
            name='isTopTen',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Топ-10'),
        ),
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.FloatField(blank=True, null=True, verbose_name='Рейтинг'),
        ),
    ]
