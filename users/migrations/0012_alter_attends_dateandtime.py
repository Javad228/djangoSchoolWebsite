# Generated by Django 3.2.13 on 2022-05-24 14:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_attends_dateandtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attends',
            name='dateAndTime',
            field=models.DateField(default=datetime.date.today, verbose_name='Session date'),
        ),
    ]