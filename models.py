# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bills(models.Model):
    billid = models.AutoField(db_column='billId', primary_key=True)  # Field name made lowercase.
    billname = models.CharField(db_column='billName', max_length=50)  # Field name made lowercase.
    billdate = models.DateField(db_column='billDate')  # Field name made lowercase.
    billprice = models.DecimalField(db_column='billPrice', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    storeid = models.ForeignKey('Storeunion', models.DO_NOTHING, db_column='storeId')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    enddate = models.DateField(db_column='endDate')  # Field name made lowercase.
    islate = models.IntegerField(db_column='isLate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bills'


class Budget(models.Model):
    budgetid = models.AutoField(db_column='budgetId', primary_key=True)  # Field name made lowercase.
    totalbills = models.DecimalField(db_column='totalBills', max_digits=10, decimal_places=2)  # Field name made lowercase.
    moneyleft = models.DecimalField(db_column='moneyLeft', max_digits=10, decimal_places=2)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    savingsmoney = models.DecimalField(db_column='savingsMoney', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'budget'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Storeunion(models.Model):
    storeid = models.AutoField(db_column='storeId', primary_key=True)  # Field name made lowercase.
    storename = models.CharField(db_column='storeName', max_length=50)  # Field name made lowercase.
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=70)
    state = models.CharField(max_length=50)
    zip = models.IntegerField()
    phonenum = models.IntegerField(db_column='phoneNum')  # Field name made lowercase.
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=100)
    iscreditunion = models.IntegerField(db_column='isCreditUnion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'storeunion'


class Users(models.Model):
    userid = models.AutoField(db_column='userId', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=40)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=50)  # Field name made lowercase.
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    phonenum = models.CharField(db_column='phoneNum', max_length=10)  # Field name made lowercase.
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_joined = models.DateTimeField()
    is_active = models.IntegerField()
    is_staff = models.IntegerField()
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class UsersGroups(models.Model):
    users_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_groups'


class UsersUserPermissions(models.Model):
    users_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_user_permissions'
