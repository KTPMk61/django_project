# Generated by Django 2.0.3 on 2018-04-13 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_student_sid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='sid',
        ),
    ]
