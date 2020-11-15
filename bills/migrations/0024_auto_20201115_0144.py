# Generated by Django 3.1.2 on 2020-11-15 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0023_auto_20201115_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='amount_remaining',
            field=models.DecimalField(db_column='amountRemaining', decimal_places=2, default=500, max_digits=10),
        ),
        migrations.AlterField(
            model_name='loan',
            name='is_late',
            field=models.BooleanField(db_column='isLate', default=False),
        ),
        migrations.AlterField(
            model_name='loan',
            name='totalamountdue',
            field=models.DecimalField(blank=True, db_column='totalAmountDue', decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='subscriptions',
            name='is_late',
            field=models.BooleanField(db_column='isLate', default=False),
        ),
    ]
