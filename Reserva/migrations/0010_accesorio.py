# Generated by Django 2.0.4 on 2018-11-18 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reserva', '0009_tarjeta_credito_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accesorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=120)),
                ('Valor', models.PositiveIntegerField()),
            ],
        ),
    ]
