# Generated by Django 2.0.3 on 2018-04-15 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_remove_student_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
