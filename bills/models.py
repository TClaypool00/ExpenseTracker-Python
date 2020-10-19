from django.db import models

from django.db import models

class Bills(models.Model):
    billid = models.AutoField(db_column='billId', primary_key=True)  # Field name made lowercase.
    billname = models.CharField(db_column='billName', max_length=50)  # Field name made lowercase.
    billdate = models.DateField(db_column='BillDate')  # Field name made lowercase.
    billprice = models.DecimalField(db_column='billPrice', max_digits=5, decimal_places=2)  # Field name made lowercase.
    islate = models.TextField(db_column='isLate')  # Field name made lowercase. This field type is a guess.
    budgetid = models.ForeignKey('Budget', models.DO_NOTHING, db_column='budgetId')  # Field name made lowercase.
    storeid = models.ForeignKey('Storeunion', models.DO_NOTHING, db_column='storeId')  # Field name made lowercase.

    class Meta:
        db_table = 'bills'
        
class Budget(models.Model):
    budgetid = models.AutoField(db_column='budgetId', primary_key=True)  # Field name made lowercase.
    totalbills = models.DecimalField(db_column='totalBills', max_digits=10, decimal_places=2)  # Field name made lowercase.
    moneyleft = models.DecimalField(db_column='moneyLeft', max_digits=10, decimal_places=2)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.

    class Meta:
        db_table = 'budget'
        
class Storeunion(models.Model):
    storeid = models.AutoField(db_column='storeId', primary_key=True)  # Field name made lowercase.
    storename = models.CharField(db_column='storeName', max_length=50)  # Field name made lowercase.
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=70)
    state = models.CharField(max_length=50)
    zip = models.IntegerField()
    phonenum = models.IntegerField(db_column='phoneNum')  # Field name made lowercase.
    email = models.CharField(max_length=30)
    website = models.CharField(max_length=50)

    class Meta:
        db_table = 'storeunion'
        
class Users(models.Model):
    userid = models.AutoField(db_column='userId', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=40)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=50)  # Field name made lowercase.
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=15)
    isadmin = models.TextField(db_column='isAdmin')  # Field name made lowercase. This field type is a guess.
    phonenum = models.IntegerField(db_column='phoneNum')  # Field name made lowercase.
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'users'
