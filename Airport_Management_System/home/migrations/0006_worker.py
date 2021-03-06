# Generated by Django 4.0.3 on 2022-04-11 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_store'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.IntegerField(default=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('payment', models.CharField(max_length=50)),
                ('job', models.CharField(max_length=50)),
                ('air_id', models.ForeignKey(default=100, on_delete=django.db.models.deletion.CASCADE, to='home.airport')),
                ('str_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.store')),
            ],
        ),
    ]
