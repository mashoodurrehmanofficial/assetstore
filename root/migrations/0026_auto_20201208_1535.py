# Generated by Django 3.1.3 on 2020-12-08 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0025_auto_20201208_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, upload_to='files/'),
        ),
    ]
