# Generated by Django 3.0.6 on 2020-06-08 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0013_gmp_questions_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='department',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='gmp_questions',
            name='created_by',
        ),
    ]