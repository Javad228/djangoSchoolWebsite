# Generated by Django 3.2.13 on 2022-05-25 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_classes_registeredstudents'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('classTaught', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.classes')),
            ],
        ),
        migrations.AddField(
            model_name='attends',
            name='taughtBy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='users.instructor'),
        ),
    ]
