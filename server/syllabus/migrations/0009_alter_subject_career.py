# Generated by Django 4.2.2 on 2023-07-21 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0008_alter_subject_career'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='career',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syllabus.career'),
        ),
    ]