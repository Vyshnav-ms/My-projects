# Generated by Django 4.2.6 on 2023-10-19 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='img',
            field=models.ImageField(default=1, upload_to='gallery'),
            preserve_default=False,
        ),
    ]
