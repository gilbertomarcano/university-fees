# Generated by Django 4.2.2 on 2023-07-21 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='prerequisites',
            field=models.TextField(blank=True, null=True),
        ),
    ]