# Generated by Django 3.1 on 2023-04-03 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinopoiskApp', '0002_auto_20230403_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.FloatField(blank=True, default=1.0, null=True, verbose_name='Рейтинг'),
        ),
    ]
