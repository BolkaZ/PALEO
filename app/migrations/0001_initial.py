# Generated by Django 5.1.1 on 2024-10-22 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название периода')),
                ('detail_text', models.TextField(verbose_name='Описание периода')),
                ('start', models.CharField(max_length=50, verbose_name='Начало периода')),
                ('end', models.CharField(max_length=50, verbose_name='Окончание периода')),
                ('found_quantity', models.PositiveIntegerField(verbose_name='Количество найденных окаменелостей')),
                ('image', models.URLField(max_length=500, verbose_name='Изображение периода')),
            ],
        ),
    ]
