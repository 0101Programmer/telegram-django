# Generated by Django 4.2.17 on 2024-12-28 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg_plus_django_app', '0044_user_alter_customuser_created_at_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.CharField(default='2024-12-28 | 07:58:16 +0300 | RTZ 2 (зима)'),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.CharField(default='2024-12-28 | 07:58:16 +0300 | RTZ 2 (зима)'),
        ),
    ]
