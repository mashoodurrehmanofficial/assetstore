# Generated by Django 3.1.3 on 2020-12-09 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0034_auto_20201208_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.FileField(blank=True, upload_to='files/'),
        ),
    ]