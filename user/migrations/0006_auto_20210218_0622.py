# Generated by Django 3.1 on 2021-02-17 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_educationprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationprofile',
            name='field_study',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='educationprofile',
            name='university_name',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
