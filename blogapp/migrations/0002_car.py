# Generated by Django 4.2.6 on 2023-10-12 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
            ],
        ),
    ]