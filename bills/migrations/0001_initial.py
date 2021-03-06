# Generated by Django 3.1.2 on 2020-10-19 19:52

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('userid', models.AutoField(db_column='userId', primary_key=True, serialize=False)),
                ('firstname', models.CharField(db_column='firstName', max_length=40)),
                ('lastname', models.CharField(db_column='lastName', max_length=50)),
                ('email', models.CharField(max_length=50, unique=True, verbose_name='email address')),
                ('password', models.CharField(max_length=15)),
                ('isadmin', models.TextField(db_column='isAdmin')),
                ('phonenum', models.IntegerField(db_column='phoneNum')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Storeunion',
            fields=[
                ('storeid', models.AutoField(db_column='storeId', primary_key=True, serialize=False)),
                ('storename', models.CharField(db_column='storeName', max_length=50)),
                ('address', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=70)),
                ('state', models.CharField(max_length=50)),
                ('zip', models.IntegerField()),
                ('phonenum', models.IntegerField(db_column='phoneNum')),
                ('email', models.CharField(max_length=30)),
                ('website', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'storeunion',
            },
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('budgetid', models.AutoField(db_column='budgetId', primary_key=True, serialize=False)),
                ('totalbills', models.DecimalField(db_column='totalBills', decimal_places=2, max_digits=10)),
                ('moneyleft', models.DecimalField(db_column='moneyLeft', decimal_places=2, max_digits=10)),
                ('userid', models.ForeignKey(db_column='userId', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'budget',
            },
        ),
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('billid', models.AutoField(db_column='billId', primary_key=True, serialize=False)),
                ('billname', models.CharField(db_column='billName', max_length=50)),
                ('billdate', models.DateField(db_column='BillDate')),
                ('billprice', models.DecimalField(db_column='billPrice', decimal_places=2, max_digits=5)),
                ('islate', models.TextField(db_column='isLate')),
                ('budgetid', models.ForeignKey(db_column='budgetId', on_delete=django.db.models.deletion.DO_NOTHING, to='bills.budget')),
                ('storeid', models.ForeignKey(db_column='storeId', on_delete=django.db.models.deletion.DO_NOTHING, to='bills.storeunion')),
            ],
            options={
                'db_table': 'bills',
            },
        ),
    ]
