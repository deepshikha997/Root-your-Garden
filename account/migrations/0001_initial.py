# Generated by Django 4.0.3 on 2022-04-27 12:53

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
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_pro', models.ImageField(default='default\\ppf.png', upload_to='media')),
                ('addr_pro', models.TextField(default='lko')),
                ('ph_pro', models.IntegerField(default='0905082929')),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
