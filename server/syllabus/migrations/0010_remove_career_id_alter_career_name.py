# Generated by Django 4.2.2 on 2023-07-21 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0009_alter_subject_career'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='career',
            name='id',
        ),
        migrations.AlterField(
            model_name='career',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
