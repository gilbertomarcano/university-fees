# Generated by Django 4.2.2 on 2023-07-10 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='course_id',
            field=models.IntegerField(default=0),
        ),
    ]
