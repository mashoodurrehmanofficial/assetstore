# Generated by Django 3.1.3 on 2020-12-08 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0022_item_querypurpose'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='AUTOSEO',
            field=models.BooleanField(default=True),
        ),
    ]
