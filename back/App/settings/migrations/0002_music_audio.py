# Generated by Django 3.2 on 2023-03-18 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='audio',
            field=models.FileField(default=1, upload_to='music'),
            preserve_default=False,
        ),
    ]