# Generated by Django 3.0.6 on 2020-06-10 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gmp_questions',
            name='compliant',
        ),
        migrations.RemoveField(
            model_name='gmp_questions',
            name='fail',
        ),
        migrations.RemoveField(
            model_name='gmp_questions',
            name='freetext',
        ),
    ]
