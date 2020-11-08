# Generated by Django 3.1.2 on 2020-11-04 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0009_auto_20201104_0300'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='savings_money',
            field=models.DecimalField(db_column='savingsMoney', decimal_places=2, default=500.0, max_digits=10),
        ),
    ]