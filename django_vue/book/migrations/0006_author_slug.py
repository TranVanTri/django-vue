# Generated by Django 4.0.6 on 2022-07-15 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_book_is_trendy'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
