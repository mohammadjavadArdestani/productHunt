# Generated by Django 3.0.3 on 2020-02-25 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200225_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='votes_total',
            field=models.IntegerField(default=1),
        ),
    ]
