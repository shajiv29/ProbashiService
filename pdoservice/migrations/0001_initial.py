# Generated by Django 2.2 on 2022-01-29 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('batch_id', models.AutoField(primary_key=True, serialize=False)),
                ('ttc_name', models.CharField(max_length=200)),
                ('batch_name', models.CharField(max_length=30)),
                ('batch_start_date', models.DateTimeField(blank=True, null=True)),
                ('class_time', models.TimeField(blank=True, null=True)),
                ('batch_slug', models.SlugField(unique=True)),
                ('is_active', models.NullBooleanField(default=True)),
                ('is_delete', models.NullBooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
