# Generated by Django 2.0.4 on 2018-11-13 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reserva', '0003_auto_20181113_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarjeta_credito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=25)),
                ('Numero_tarjeta_redito', models.CharField(max_length=19)),
                ('Fecha_vencimiento', models.DateField()),
            ],
        ),
    ]