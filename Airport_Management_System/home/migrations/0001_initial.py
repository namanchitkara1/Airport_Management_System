# Generated by Django 4.0.3 on 2022-03-28 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('air_id', models.IntegerField(default=100, primary_key=True, serialize=False)),
                ('airport_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
