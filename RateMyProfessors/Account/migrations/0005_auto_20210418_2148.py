# Generated by Django 3.1.7 on 2021-04-18 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_auto_20210417_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]