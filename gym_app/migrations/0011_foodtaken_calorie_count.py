# Generated by Django 3.2.5 on 2021-10-14 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0010_foodtaken'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodtaken',
            name='calorie_count',
            field=models.IntegerField(default=0),
        ),
    ]
