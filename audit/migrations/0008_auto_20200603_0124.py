# Generated by Django 3.0.6 on 2020-06-03 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0007_auto_20200603_0121'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='areas',
            new_name='area',
        ),
        migrations.AlterField(
            model_name='gmp_questions',
            name='created_by',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
