# Generated by Django 3.2.12 on 2023-07-01 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teste', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Antropometria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('massacorporal', models.DecimalField(decimal_places=2, max_digits=5)),
                ('dctriceps', models.CharField(max_length=4)),
                ('dcabdominal', models.CharField(max_length=4)),
                ('dcpanturrilha', models.CharField(max_length=4)),
                ('dcsubescapular', models.CharField(max_length=4)),
                ('circcoxamedial', models.CharField(max_length=4)),
                ('circpanturmedial', models.CharField(max_length=4)),
                ('dcbiceps', models.CharField(max_length=4)),
                ('dcpeitoral', models.CharField(max_length=4)),
                ('dccoxamedial', models.CharField(max_length=4)),
                ('dcsuprailiaca', models.CharField(max_length=4)),
                ('dccoxaproximal', models.CharField(max_length=4)),
                ('dcmedioaxilar', models.CharField(max_length=4)),
                ('teste', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='teste.teste')),
            ],
            options={
                'verbose_name': 'Antropometria',
            },
        ),
    ]
