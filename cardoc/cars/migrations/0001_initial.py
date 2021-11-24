# Generated by Django 3.2.7 on 2021-11-24 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=None, null=True)),
                ('model', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'cars',
            },
        ),
        migrations.CreateModel(
            name='Trim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=None, null=True)),
                ('name', models.CharField(max_length=50)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
            options={
                'db_table': 'trims',
            },
        ),
        migrations.CreateModel(
            name='Tire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=None, null=True)),
                ('position', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('width', models.IntegerField()),
                ('aspect_ratio', models.IntegerField()),
                ('wheel_size', models.IntegerField()),
                ('trim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.trim')),
            ],
            options={
                'db_table': 'tires',
            },
        ),
    ]