# Generated by Django 4.2.17 on 2024-12-28 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg_plus_django_app', '0042_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField()),
                ('tg_username', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
                ('orders', models.JSONField(blank=True, null=True)),
                ('created_at', models.CharField(default='2024-12-28 | 07:51:20 +0300 | RTZ 2 (зима)')),
                ('updated_at', models.CharField(default='2024-12-28 | 07:51:20 +0300 | RTZ 2 (зима)')),
                ('user_data', models.JSONField(blank=True, null=True)),
                ('is_active', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
