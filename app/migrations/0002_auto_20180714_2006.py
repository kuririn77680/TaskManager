# Generated by Django 2.0.6 on 2018-07-14 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='action',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='task',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
