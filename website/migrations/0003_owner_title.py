# Generated by Django 5.0.6 on 2024-07-15 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_owner_hero_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='title',
            field=models.CharField(default='Eng. Makasa', max_length=64),
            preserve_default=False,
        ),
    ]
