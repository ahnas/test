# Generated by Django 3.2.5 on 2021-07-15 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20210715_1506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='wnumber',
            new_name='whatsapp_number',
        ),
    ]