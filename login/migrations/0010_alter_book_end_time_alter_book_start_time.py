# Generated by Django 4.0.3 on 2022-07-28 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_alter_book_require'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='start_time',
            field=models.DateField(),
        ),
    ]
