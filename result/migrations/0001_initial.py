# Generated by Django 3.1.5 on 2021-02-26 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matching_Table',
            fields=[
                ('user_man_id', models.TextField(primary_key=True, serialize=False)),
                ('user_woman_id', models.TextField()),
            ],
        ),
    ]
