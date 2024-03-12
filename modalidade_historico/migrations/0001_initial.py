# Generated by Django 4.2.2 on 2023-08-11 17:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('atleta', '0001_initial'),
        ('usuario', '0002_usuario_administrador'),
        ('modalidade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modalidade_historico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vigencia_inicial', models.CharField(max_length=100)),
                ('vigencia_final', models.DateField(default=datetime.date.today)),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('atleta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='atleta.atleta')),
                ('modalidade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='modalidade.modalidade')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.usuario')),
            ],
            options={
                'verbose_name': 'Modalidade historico',
            },
        ),
    ]
