# Generated by Django 5.1.5 on 2025-01-26 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default='Hola'),
            preserve_default=False,
        ),
    ]
