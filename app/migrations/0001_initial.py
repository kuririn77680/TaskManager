# Generated by Django 2.0.6 on 2018-07-14 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=255, verbose_name='action')),
                ('done', models.BooleanField(default=False, verbose_name='Done?')),
                ('priority', models.IntegerField(unique=True, verbose_name='priority')),
            ],
        ),
    ]