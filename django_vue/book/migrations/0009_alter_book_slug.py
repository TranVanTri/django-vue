# Generated by Django 4.0.6 on 2022-07-15 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_remove_book_thumbnail_alter_book_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, default='s'),
        ),
    ]
