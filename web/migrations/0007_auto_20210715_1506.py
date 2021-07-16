# Generated by Django 3.2.5 on 2021-07-15 09:36

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_award'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='wnumber',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='award',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(upload_to='award'),
        ),
    ]