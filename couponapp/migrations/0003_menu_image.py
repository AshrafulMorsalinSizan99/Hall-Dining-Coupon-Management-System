# Generated by Django 4.1.1 on 2023-03-18 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couponapp', '0002_alter_menu_menutype'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
