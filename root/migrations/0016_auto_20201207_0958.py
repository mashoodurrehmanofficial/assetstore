# Generated by Django 3.1.3 on 2020-12-07 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0015_auto_20201207_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='storelink',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
