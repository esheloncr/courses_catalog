# Generated by Django 3.1.5 on 2021-01-19 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20210119_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_url',
            field=models.URLField(default='#'),
        ),
    ]
