# Generated by Django 5.1.4 on 2025-01-23 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0002_profile_name_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pics/default.png', null=True, upload_to='profile_pics'),
        ),
    ]
