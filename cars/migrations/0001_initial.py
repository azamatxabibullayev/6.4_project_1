# Generated by Django 5.0.4 on 2024-05-04 21:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('make', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('year', models.IntegerField()),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='cars/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.category')),
            ],
            options={
                'db_table': 'Car',
            },
        ),
    ]
