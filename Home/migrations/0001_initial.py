# Generated by Django 4.0.3 on 2022-05-12 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cat', models.CharField(max_length=25)),
                ('image_cat', models.ImageField(upload_to='media')),
                ('desc_cat', models.TextField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nursery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_nur', models.CharField(max_length=25)),
                ('image_nur', models.ImageField(upload_to='media')),
                ('desc_nur', models.TextField()),
                ('servicecharge', models.IntegerField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('cate', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Home.category')),
                ('usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ser', models.CharField(max_length=25)),
                ('desc_ser', models.TextField()),
                ('price_ser', models.IntegerField()),
                ('img_ser', models.ImageField(upload_to='media')),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('cate', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Home.nursery')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_ids', models.CharField(max_length=250)),
                ('product_ids', models.CharField(max_length=250)),
                ('invoice_id', models.CharField(max_length=250)),
                ('status', models.BooleanField(default=False)),
                ('processed_on', models.DateTimeField(auto_now_add=True)),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.BigIntegerField()),
                ('msg', models.TextField()),
                ('usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('added_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_on', models.DateTimeField(auto_now=True, null=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.service')),
                ('usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]