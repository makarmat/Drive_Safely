# Generated by Django 2.2.7 on 2019-11-26 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drive_safely_api', '0002_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='advice',
            name='photo',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='drive_safely_api.Photo'),
            preserve_default=False,
        ),
    ]