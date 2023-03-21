# Generated by Django 3.2 on 2023-03-19 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_music_audio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='music',
            name='colors',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='settings.color'),
            preserve_default=False,
        ),
    ]
