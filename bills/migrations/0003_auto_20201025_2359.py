# Generated by Django 3.1.2 on 2020-10-26 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0002_auto_20201023_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phonenum',
            field=models.CharField(db_column='phoneNum', max_length=10),
        ),
    ]