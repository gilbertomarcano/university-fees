# Generated by Django 4.2.2 on 2023-07-09 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=10)),
                ('course', models.CharField(max_length=10)),
                ('grade', models.FloatField()),
            ],
        ),
    ]