# Generated by Django 3.1.3 on 2021-01-18 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210118_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookshop',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
