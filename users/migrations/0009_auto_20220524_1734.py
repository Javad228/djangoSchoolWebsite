# Generated by Django 3.2.13 on 2022-05-24 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20220524_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='attends',
            name='isAbsent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='attends',
            name='isLate',
            field=models.BooleanField(default=False),
        ),
    ]
