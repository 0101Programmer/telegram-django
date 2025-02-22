# Generated by Django 4.2.17 on 2025-01-11 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg_plus_django_app', '0014_delete_product'),
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
                ('ratings', models.JSONField(blank=True, null=True)),
                ('images_paths', models.JSONField()),
            ],
        ),
    ]
