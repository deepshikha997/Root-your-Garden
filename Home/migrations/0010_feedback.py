# Generated by Django 4.0.3 on 2022-05-31 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_profile_ph_pro'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home', '0009_delete_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=250)),
                ('msg', models.TextField()),
                ('added_on', models.DateTimeField(auto_now=True, null=True)),
                ('prf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
