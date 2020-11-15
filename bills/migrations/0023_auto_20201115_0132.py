# Generated by Django 3.1.2 on 2020-11-15 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0022_remove_bills_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bills',
            name='is_paid',
            field=models.BooleanField(db_column='isPaid', default=False),
        ),
        migrations.AddField(
            model_name='loan',
            name='amount_remaining',
            field=models.FloatField(db_column='amountRemaining', default=500),
        ),
        migrations.AddField(
            model_name='loan',
            name='is_late',
            field=models.BooleanField(db_column='iLate', default=False),
        ),
        migrations.AddField(
            model_name='loan',
            name='is_paid',
            field=models.BooleanField(db_column='isPaid', default=False),
        ),
        migrations.AddField(
            model_name='subscriptions',
            name='is_late',
            field=models.BooleanField(db_column='iLate', default=False),
        ),
        migrations.AddField(
            model_name='subscriptions',
            name='is_paid',
            field=models.BooleanField(db_column='isPaid', default=False),
        ),
        migrations.AlterField(
            model_name='storeunion',
            name='is_completed',
            field=models.BooleanField(db_column='isCompleted', default=True),
        ),
    ]
