# Generated by Django 2.0.4 on 2018-11-13 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reserva', '0004_tarjeta_credito'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_arriendo_inicial', models.DateField()),
                ('Hora_arriendo_inicial', models.TimeField()),
                ('Fecha_arriendo_final', models.DateField()),
                ('Hora_arriendo_final', models.TimeField()),
                ('Sucursal_fin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserva_fin', to='Reserva.Sucursal')),
                ('Sucursal_inicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserva_inicio', to='Reserva.Sucursal')),
            ],
        ),
    ]
