# Generated by Django 3.0.6 on 2020-06-02 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='street_address1',
            new_name='street_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='street_address2',
        ),
    ]
