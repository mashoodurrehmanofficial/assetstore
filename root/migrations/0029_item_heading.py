# Generated by Django 3.1.3 on 2020-12-08 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0028_auto_20201208_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='heading',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
