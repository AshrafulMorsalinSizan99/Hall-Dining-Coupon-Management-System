# Generated by Django 4.1.1 on 2023-03-18 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('couponapp', '0003_menu_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='addons',
            name='hall',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='couponapp.hall'),
        ),
    ]
