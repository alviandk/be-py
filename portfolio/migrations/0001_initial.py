# Generated by Django 3.1 on 2021-02-08 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('url', models.URLField(blank=True, null=True)),
                ('cover_image', models.ImageField(upload_to='')),
                ('git_url', models.URLField()),
                ('slug', models.SlugField(default='')),
                ('ordering', models.IntegerField(default=0)),
            ],
        ),
    ]