# Generated by Django 3.1.7 on 2021-04-10 09:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0017_auto_20210410_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancel_order_for_money_back',
            name='Cancel_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 10, 15, 25, 20, 676988)),
        ),
    ]