# Generated by Django 2.2.7 on 2019-11-26 18:58

from django.db import migrations, models
import drive_safely_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('drive_safely_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(height_field='height', upload_to=drive_safely_api.models.images_upload_path, width_field='width')),
                ('width', models.IntegerField(editable=False)),
                ('height', models.IntegerField(editable=False)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
