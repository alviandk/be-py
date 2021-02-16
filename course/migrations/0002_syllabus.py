# Generated by Django 3.1 on 2021-02-16 13:52

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectives', ckeditor.fields.RichTextField()),
                ('technologies', ckeditor.fields.RichTextField()),
                ('prerequisites', ckeditor.fields.RichTextField()),
                ('version', ckeditor.fields.RichTextField()),
                ('source', ckeditor.fields.RichTextField()),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='syllabus', to='course.course')),
            ],
        ),
    ]
