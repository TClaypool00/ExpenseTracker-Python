from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class Bills(models.Model):
    billid = models.AutoField(db_column='billId', primary_key=True)  # Field name made lowercase.
    billname = models.CharField(db_column='billName', max_length=50)  # Field name made lowercase.
    billdate = models.DateField(db_column='BillDate')  # Field name made lowercase.
    billprice = models.DecimalField(db_column='billPrice', max_digits=5, decimal_places=2)  # Field name made lowercase.
    islate = models.BooleanField(db_column='isLate', default=False)  # Field name made lowercase. This field type is a guess.
    end_date = models.DateField(db_column='endDate', default='2020-11-6')
    budgetid = models.ForeignKey('Budget', models.DO_NOTHING, db_column='budgetId')  # Field name made lowercase.
    storeid = models.ForeignKey('Storeunion', models.DO_NOTHING, db_column='storeId')  # Field name made lowercase.

    class Meta:
        db_table = 'bills'
        
class Budget(models.Model):
    budgetid = models.AutoField(db_column='budgetId', primary_key=True)  # Field name made lowercase.
    totalbills = models.DecimalField(db_column='totalBills', max_digits=10, decimal_places=2)  # Field name made lowercase.
    moneyleft = models.DecimalField(db_column='moneyLeft', max_digits=10, decimal_places=2)  # Field name made lowercase.
    savings_money = models.DecimalField(db_column='savingsMoney', max_digits=10, decimal_places=2, default=500.00)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.

    class Meta:
        db_table = 'budget'
        
class Storeunion(models.Model):
    storeid = models.AutoField(db_column='storeId', primary_key=True)  # Field name made lowercase.
    storename = models.CharField(db_column='storeName', max_length=50)  # Field name made lowercase.
    address = models.CharField(max_length=60, null=True)
    city = models.CharField(max_length=70, null=True)
    state = models.CharField(max_length=50, null=True)
    zip = models.IntegerField(null=True)
    phonenum = models.IntegerField(db_column='phoneNum', null=True)  # Field name made lowercase.
    email = models.CharField(max_length=50, null=True)
    website = models.CharField(max_length=100)
    is_credit_union = models.BooleanField(db_column='isCreditUnion', default=False)
    is_completed = models.BooleanField(db_column="IsCompleted", default=True)

    class Meta:
        db_table = 'storeunion'
        
class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
        
class Users(AbstractUser):
    userid = models.AutoField(db_column='userId', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=40)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=50)  # Field name made lowercase.
    email = models.CharField(_('email address'), unique=True, max_length=50)
    password = models.CharField(db_column='password',max_length=128)
    phonenum = models.CharField(db_column='phoneNum', max_length=10)  # Field name made lowercase.
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    username = None
    first_name = None
    last_name = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()

    class Meta:
        db_table = 'users'
        
        
class Misc(models.Model):
    miscid = models.AutoField(db_column='miscId', primary_key=True)  # Field name made lowercase.
    misc_name = models.CharField(db_column='miscName', max_length=100, default='Groceries')
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    storeid = models.ForeignKey('Storeunion', models.DO_NOTHING, db_column='storeId')  # Field name made lowercase.
    date = models.DateField()
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userId', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'misc'
        
        
class Subscriptions(models.Model):
    subid = models.AutoField(db_column='subId', primary_key=True)  # Field name made lowercase.
    duedate = models.DateField(db_column='dueDate')  # Field name made lowercase.
    amountdue = models.DecimalField(db_column='amountDue', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    storeid = models.ForeignKey(Storeunion, models.DO_NOTHING, db_column='storeId')  # Field name made lowercase.
    subname = models.CharField(db_column='subName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'subscriptions'