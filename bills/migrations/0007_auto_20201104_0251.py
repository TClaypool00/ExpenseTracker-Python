# Generated by Django 3.1.2 on 2020-11-04 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0006_auto_20201026_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='users',
            name='isadmin',
        ),
        migrations.RemoveField(
            model_name='users',
            name='last_name',
        ),
    ]