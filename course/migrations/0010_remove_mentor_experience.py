# Generated by Django 3.1 on 2021-02-18 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_auto_20210218_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='experience',
        ),
    ]
