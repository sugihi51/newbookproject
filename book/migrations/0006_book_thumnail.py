# Generated by Django 5.1.2 on 2025-05-29 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='thumnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
