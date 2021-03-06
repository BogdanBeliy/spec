# Generated by Django 3.2.12 on 2022-03-11 14:11

import account.managers
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermodel',
            options={},
        ),
        migrations.AlterModelManagers(
            name='usermodel',
            managers=[
                ('objects', account.managers.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='date_joined',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 11, 14, 11, 48, 682697, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 11, 14, 11, 48, 682797, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='PersonalArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(choices=[('free', 'free'), ('payment', 'payment')], default=('free', 'free'), max_length=100)),
                ('check', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('logo', models.ImageField(upload_to='logos/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='personal_area', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
