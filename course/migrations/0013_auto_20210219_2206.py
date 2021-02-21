# Generated by Django 3.1 on 2021-02-19 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_auto_20210219_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='learn_type',
            field=models.CharField(choices=[('MDR', 'Mandiri'), ('GRP', 'Group')], default='MDR', max_length=8),
        ),
        migrations.AlterField(
            model_name='collegeproject',
            name='status',
            field=models.CharField(choices=[('WTG', 'Waiting'), ('APR', 'Approved'), ('RJT', 'Rejected')], default='WTG', max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='mentoringrequest',
            name='status',
            field=models.CharField(choices=[('WTG', 'Waiting'), ('APR', 'Approved'), ('RJT', 'Rejected')], default='WTG', max_length=8, null=True),
        ),
    ]