# Generated by Django 4.2.17 on 2024-12-21 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg_plus_django_app', '0029_delete_product_alter_user_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('model_name', models.TextField()),
                ('model_name_for_customer', models.TextField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('category', models.CharField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.CharField(default='2024-12-21 | 07:05:10 +0300 | RTZ 2 (зима)'),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.CharField(default='2024-12-21 | 07:05:10 +0300 | RTZ 2 (зима)'),
        ),
    ]
