# Generated by Django 3.2.7 on 2022-01-04 05:51

import datetime
from django.conf import settings
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
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('name', models.CharField(default='admin', max_length=160)),
                ('phone', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('address', models.TextField(db_index=True, max_length=200)),
                ('pin_code', models.IntegerField(db_index=True)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(db_index=True, max_length=100)),
                ('city', models.CharField(db_index=True, max_length=100)),
                ('tax1', models.CharField(db_index=True, max_length=50)),
                ('tax2', models.CharField(db_index=True, max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='userBusiness', to=settings.AUTH_USER_MODEL)),
                ('parent_company', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='parent', to='api.business')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categories_created_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(db_index=True, max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pageCreated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(db_index=True, max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='userRoleCreate', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserRoles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='business', to='api.business')),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='userRole', to=settings.AUTH_USER_MODEL)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='role', to='api.role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='unitCreatedUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short_name', models.CharField(max_length=100)),
                ('tax_percentage', models.FloatField(default=0.0)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='taxCreatedUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='category', to='api.categories')),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subcategories_created_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RolePermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read', models.BooleanField(db_index=True, default=False)),
                ('create', models.BooleanField(db_index=True, default=False)),
                ('delete', models.BooleanField(db_index=True, default=False)),
                ('update', models.BooleanField(db_index=True, default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rolePermission', to=settings.AUTH_USER_MODEL)),
                ('page_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pages', to='api.pages')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='roleMap', to='api.role')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('purchase_rate', models.FloatField(blank=True, db_index=True, null=True)),
                ('mrp', models.FloatField(blank=True, db_index=True, null=True)),
                ('sales_percentage', models.FloatField(blank=True, db_index=True, null=True)),
                ('sales_rate', models.FloatField(blank=True, db_index=True, null=True)),
                ('tax_rate', models.FloatField(blank=True, db_index=True, null=True)),
                ('duration', models.FloatField(blank=True, db_index=True, null=True)),
                ('expiry_date', models.DateField(blank=True, db_index=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_created_user', to=settings.AUTH_USER_MODEL)),
                ('subCategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sub_category', to='api.subcategories')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_image_created_user', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='prodcut_image', to='api.products')),
            ],
        ),
        migrations.CreateModel(
            name='Desingation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='userDesingationCreate', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DefaultBusiness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defualt_business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='defualtBusiness', to='api.business')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='defaultBusUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('age', models.IntegerField(default=0)),
                ('phone', models.CharField(max_length=20)),
                ('blood', models.CharField(max_length=20, null=True)),
                ('country', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('pincode', models.IntegerField(default=0)),
                ('address', models.TextField(max_length=250)),
                ('insurance_comapny', models.CharField(max_length=150)),
                ('insurance_expiry', models.DateField()),
                ('insurance_num', models.CharField(db_index=True, max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='customerCreatedUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField(default=datetime.date.today)),
                ('proposed_fee', models.FloatField()),
                ('customer_fee', models.FloatField()),
                ('amount_paid', models.FloatField()),
                ('due_amount', models.FloatField()),
                ('reminder_date', models.DateField()),
                ('notes', models.TextField()),
                ('status', models.CharField(default='P', max_length=3)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='appointmentCreatedUser', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='customer', to='api.customers')),
                ('initial_consultant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='initial_cosultant', to=settings.AUTH_USER_MODEL)),
                ('main_consultant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='main_cosultant', to=settings.AUTH_USER_MODEL)),
                ('refferd_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='refferdBy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='designation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='UserDesignation', to='api.desingation'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
