# Generated by Django 3.1.3 on 2020-12-07 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0019_item_latestversion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Compatibility',
            new_name='compatibility',
        ),
    ]
