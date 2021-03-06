# Generated by Django 2.2 on 2022-01-30 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_permanentaddress_presentaddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('district_name', models.CharField(max_length=20)),
                ('is_active', models.NullBooleanField(default=False)),
                ('is_delete', models.NullBooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('division_name', models.CharField(max_length=20)),
                ('is_active', models.NullBooleanField(default=False)),
                ('is_delete', models.NullBooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Upazila',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('upazila_name', models.CharField(max_length=20)),
                ('is_active', models.NullBooleanField(default=False)),
                ('is_delete', models.NullBooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now_add=True, null=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.District')),
            ],
        ),
        migrations.CreateModel(
            name='Thana',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('thana_name', models.CharField(max_length=20)),
                ('is_active', models.NullBooleanField(default=False)),
                ('is_delete', models.NullBooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now_add=True, null=True)),
                ('upazila', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Upazila')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Division'),
        ),
    ]
