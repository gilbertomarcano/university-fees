# Generated by Django 4.2.2 on 2023-07-09 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='enrollment',
            field=models.IntegerField(blank=True),
        ),
    ]
