# Generated by Django 2.2 on 2022-01-30 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20220131_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='PresentAddress',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('division', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('upazila', models.CharField(max_length=20)),
                ('thana', models.CharField(max_length=20)),
                ('village', models.CharField(max_length=20)),
                ('house_no', models.CharField(max_length=20)),
                ('zip_code', models.CharField(max_length=20)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
        migrations.CreateModel(
            name='PermanentAddress',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('division', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('upazila', models.CharField(max_length=20)),
                ('thana', models.CharField(max_length=20)),
                ('village', models.CharField(max_length=20)),
                ('house_no', models.CharField(max_length=20)),
                ('zip_code', models.CharField(max_length=20)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
    ]
