# Generated by Django 3.2.5 on 2021-10-13 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('category', models.CharField(choices=[('veg', 'Veg'), ('nonveg', 'Non-Veg')], max_length=50)),
                ('goal', models.CharField(choices=[('gain', 'Gain Weight'), ('loss', 'Lose Weight')], max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
