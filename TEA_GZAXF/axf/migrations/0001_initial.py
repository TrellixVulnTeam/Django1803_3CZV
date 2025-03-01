# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-25 13:22
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.CharField(max_length=100, unique=True)),
                ('icon', models.ImageField(upload_to='icon')),
                ('phone', models.CharField(blank=True, max_length=13, null=True)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='地址说明')),
                ('lat', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='纬度')),
                ('lng', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='经度')),
                ('is_default', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='商品数量')),
                ('is_select', models.BooleanField(default=True, verbose_name='选中状态')),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=10)),
                ('productimg', models.CharField(max_length=200)),
                ('productname', models.CharField(max_length=100)),
                ('productlongname', models.CharField(max_length=255)),
                ('isxf', models.BooleanField()),
                ('pmdesc', models.IntegerField()),
                ('specifics', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('marketprice', models.FloatField()),
                ('categoryid', models.IntegerField()),
                ('childcid', models.IntegerField()),
                ('childcidname', models.CharField(max_length=100)),
                ('dealerid', models.CharField(max_length=30)),
                ('storenums', models.IntegerField()),
                ('productnum', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_goods',
            },
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=20)),
                ('typename', models.CharField(max_length=30)),
                ('childtypenames', models.CharField(max_length=255)),
                ('typesort', models.IntegerField()),
            ],
            options={
                'verbose_name': '商品分类',
                'db_table': 'axf_foodtypes',
            },
        ),
        migrations.CreateModel(
            name='MainShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trackid', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('img', models.CharField(max_length=200)),
                ('categoryid', models.CharField(max_length=200)),
                ('brandname', models.CharField(max_length=200)),
                ('img1', models.CharField(max_length=200)),
                ('childcid1', models.CharField(max_length=200)),
                ('productid1', models.CharField(max_length=200)),
                ('longname1', models.CharField(max_length=200)),
                ('price1', models.CharField(max_length=200)),
                ('marketprice1', models.CharField(max_length=200)),
                ('img2', models.CharField(max_length=200)),
                ('childcid2', models.CharField(max_length=200)),
                ('productid2', models.CharField(max_length=200)),
                ('longname2', models.CharField(max_length=200)),
                ('price2', models.CharField(max_length=200)),
                ('marketprice2', models.CharField(max_length=200)),
                ('img3', models.CharField(max_length=200)),
                ('childcid3', models.CharField(max_length=200)),
                ('productid3', models.CharField(max_length=200)),
                ('longname3', models.CharField(max_length=200)),
                ('price3', models.CharField(max_length=200)),
                ('marketprice3', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MustBuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=255, verbose_name='图片')),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '必购',
                'db_table': 'axf_mustbuy',
            },
        ),
        migrations.CreateModel(
            name='MyNav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=255, verbose_name='图片')),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '导航数据',
                'db_table': 'axf_nav',
            },
        ),
        migrations.CreateModel(
            name='MyShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=255, verbose_name='图片')),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '商店',
                'db_table': 'axf_shop',
            },
        ),
        migrations.CreateModel(
            name='MyWheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=255, verbose_name='图片')),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '轮播数据',
                'db_table': 'axf_wheel',
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axf.Goods', verbose_name='商品'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='axf.Address'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together=set([('goods', 'user')]),
        ),
        migrations.AlterIndexTogether(
            name='cart',
            index_together=set([('user', 'goods')]),
        ),
    ]
