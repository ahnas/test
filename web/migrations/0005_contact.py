# Generated by Django 3.2.5 on 2021-07-15 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
