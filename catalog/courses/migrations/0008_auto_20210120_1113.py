# Generated by Django 3.1.5 on 2021-01-20 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20210120_1112'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Курс', 'verbose_name_plural': 'Курсы'},
        ),
    ]