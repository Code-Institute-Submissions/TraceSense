# Generated by Django 3.0.6 on 2020-06-12 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('contact_name', models.CharField(max_length=55)),
                ('contact_email', models.EmailField(max_length=55)),
                ('enquiry_details', models.CharField(max_length=255)),
            ],
        ),
    ]
