# Generated by Django 3.1.7 on 2021-04-07 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0001_initial'),
        ('home', '0004_customer_more_information'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='Intructor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='instructor.instructor_information'),
            preserve_default=False,
        ),
    ]