# Generated by Django 3.1.3 on 2020-12-08 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0030_item_autogenrate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='shortname',
            new_name='url',
        ),
        migrations.AlterField(
            model_name='item',
            name='AUTOGENRATE',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
