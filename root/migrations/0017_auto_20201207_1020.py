# Generated by Django 3.1.3 on 2020-12-07 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0016_auto_20201207_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='filesize',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='item',
            name='version',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
