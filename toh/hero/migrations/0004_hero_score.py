# Generated by Django 3.1.1 on 2020-10-15 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0003_auto_20201015_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]