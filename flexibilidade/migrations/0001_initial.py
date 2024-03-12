# Generated by Django 3.2.12 on 2023-07-01 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teste', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flexibilidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wells_1', models.CharField(max_length=15)),
                ('wells_2', models.CharField(max_length=15)),
                ('wells_3', models.CharField(max_length=15)),
                ('teste', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='teste.teste')),
            ],
            options={
                'verbose_name': 'Flexibilidade',
            },
        ),
    ]
