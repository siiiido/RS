# Generated by Django 3.1.5 on 2021-02-20 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_auto_20210219_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social_user_table',
            name='image',
            field=models.ImageField(blank=True, upload_to='social'),
        ),
    ]
