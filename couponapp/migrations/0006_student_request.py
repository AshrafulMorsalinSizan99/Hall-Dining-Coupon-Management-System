# Generated by Django 4.1.1 on 2023-03-19 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couponapp', '0005_department_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='request',
            field=models.IntegerField(default=0),
        ),
    ]
