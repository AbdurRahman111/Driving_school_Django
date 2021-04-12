# Generated by Django 3.1.7 on 2021-04-10 09:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0015_auto_20210410_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='cancel_order_for_money_back',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cancel_Time', models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 10, 15, 5, 21, 325014))),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
