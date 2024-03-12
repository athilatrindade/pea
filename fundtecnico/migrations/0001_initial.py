# Generated by Django 3.2.12 on 2023-07-01 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teste', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fundtecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('controle_1', models.CharField(max_length=15)),
                ('controle_2', models.CharField(max_length=15)),
                ('controle_3', models.CharField(max_length=15)),
                ('passe_1', models.CharField(max_length=15)),
                ('passe_2', models.CharField(max_length=15)),
                ('passe_3', models.CharField(max_length=15)),
                ('conducao_1', models.CharField(max_length=15)),
                ('conducao_2', models.CharField(max_length=15)),
                ('conducao_3', models.CharField(max_length=15)),
                ('chute_1', models.CharField(max_length=15)),
                ('chute_2', models.CharField(max_length=15)),
                ('chute_3', models.CharField(max_length=15)),
                ('teste', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='teste.teste')),
            ],
            options={
                'verbose_name': 'Fundtecnico',
            },
        ),
    ]
