# Generated by Django 4.2.2 on 2023-10-23 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0001_initial'),
        ('antropometria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalculoAntropometria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('somanovedobras', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('somasetedobras', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('densicorphomem', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('densicorpmulher', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('percgordhomem', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('percgordmulher', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('teste', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='teste.teste')),
            ],
            options={
                'verbose_name': 'CalculoAntropometria',
            },
        ),
    ]
