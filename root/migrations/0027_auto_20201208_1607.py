# Generated by Django 3.1.3 on 2020-12-08 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0026_auto_20201208_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
