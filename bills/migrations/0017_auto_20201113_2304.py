# Generated by Django 3.1.2 on 2020-11-14 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0016_auto_20201108_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeunion',
            name='is_completed',
            field=models.BooleanField(db_column='IsCompleted', default=True),
        ),
        migrations.AlterField(
            model_name='storeunion',
            name='address',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='storeunion',
            name='city',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='storeunion',
            name='phonenum',
            field=models.IntegerField(db_column='phoneNum', null=True),
        ),
        migrations.AlterField(
            model_name='storeunion',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='storeunion',
            name='zip',
            field=models.IntegerField(null=True),
        ),
    ]
