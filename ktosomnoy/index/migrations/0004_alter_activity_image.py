# Generated by Django 5.1.7 on 2025-03-26 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_alter_activity_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='image',
            field=models.ImageField(default='', upload_to='static/img'),
        ),
    ]
