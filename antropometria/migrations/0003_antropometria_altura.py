# Generated by Django 4.2.2 on 2023-10-26 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antropometria', '0002_calculoantropometria'),
    ]

    operations = [
        migrations.AddField(
            model_name='antropometria',
            name='altura',
            field=models.CharField(blank=True, max_length=3),
        ),
    ]
