# Generated by Django 3.2.5 on 2021-07-15 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_alter_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]
