# Generated by Django 3.1.7 on 2021-04-09 05:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20210409_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product_details',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 4, 9, 11, 29, 48, 386529)),
        ),
    ]
