# Generated by Django 3.1.3 on 2020-12-06 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_auto_20201206_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='TEST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='insertTOP',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.IntegerField(default=1607266418, primary_key=True, serialize=False),
        ),
    ]
