# Generated by Django 2.0.3 on 2018-04-14 02:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_student_khoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='bir',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]