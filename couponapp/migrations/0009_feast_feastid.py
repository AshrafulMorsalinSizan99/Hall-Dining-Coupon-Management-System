# Generated by Django 4.1.1 on 2023-03-21 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couponapp', '0008_feast'),
    ]

    operations = [
        migrations.AddField(
            model_name='feast',
            name='feastId',
            field=models.IntegerField(default=0),
        ),
    ]
