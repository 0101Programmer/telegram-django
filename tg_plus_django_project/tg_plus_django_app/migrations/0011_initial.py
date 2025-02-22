# Generated by Django 4.2.17 on 2025-01-09 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tg_plus_django_app', '0010_delete_product_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('category', models.CharField()),
                ('brand', models.CharField()),
                ('images_paths', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField()),
                ('tg_username', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
                ('orders', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
