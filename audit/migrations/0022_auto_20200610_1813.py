# Generated by Django 3.0.6 on 2020-06-10 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0021_auto_20200610_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gmp_questions',
            name='user',
        ),
        migrations.DeleteModel(
            name='gmp_answers',
        ),
        migrations.DeleteModel(
            name='gmp_questions',
        ),
    ]