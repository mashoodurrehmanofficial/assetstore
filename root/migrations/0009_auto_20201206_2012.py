# Generated by Django 3.1.3 on 2020-12-06 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0008_auto_20201206_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='test',
            name='id',
            field=models.IntegerField(default=100000, primary_key=True, serialize=False),
        ),
    ]
