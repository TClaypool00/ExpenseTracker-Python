# Generated by Django 3.1.2 on 2020-11-08 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0014_misc'),
    ]

    operations = [
        migrations.AddField(
            model_name='misc',
            name='memo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='misc',
            name='misc_name',
            field=models.CharField(blank=True, db_column='miscName', max_length=100, null=True),
        ),
    ]
