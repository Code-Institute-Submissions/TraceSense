# Generated by Django 3.0.6 on 2020-06-03 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0006_auto_20200603_0115'),
    ]

    operations = [
        migrations.CreateModel(
            name='areas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='gmp_questions',
            name='created_by',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]