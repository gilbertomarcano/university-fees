# Generated by Django 4.2.2 on 2023-07-09 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_alter_payment_enrollment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Enrollment',
        ),
    ]
