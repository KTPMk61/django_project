# Generated by Django 2.0.3 on 2018-04-13 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_student_sid'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='sid',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]