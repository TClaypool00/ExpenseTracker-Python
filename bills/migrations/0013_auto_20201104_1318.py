# Generated by Django 3.1.2 on 2020-11-04 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0012_auto_20201104_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='islate',
            field=models.BooleanField(db_column='isLate', default=False),
        ),
    ]
