# Generated by Django 4.0.6 on 2023-03-09 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lynx', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='Default.jpg', null=True, upload_to=''),
        ),
    ]
