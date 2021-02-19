# Generated by Django 3.1 on 2021-02-18 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_remove_experience_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='Experience',
        ),
        migrations.AddField(
            model_name='mentor',
            name='experience',
            field=models.ManyToManyField(blank=True, related_name='mentors', to='course.Experience'),
        ),
    ]