# Generated by Django 2.0.3 on 2018-03-24 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Mocion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('contenido', models.TextField()),
                ('presupuesto', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('estado', models.CharField(choices=[('propuesta', 'Propuesta de usuario'), ('discusion', 'En discusión del congreso'), ('aprobado_p', 'Propuesta aprobada'), ('aprobado_d', 'Discusión aprobada'), ('rechazado_p', 'Propuesta rechazada'), ('rechazado_d', 'Discusión rechazada')], default='propuesta', max_length=20)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mociones.Categoria')),
            ],
        ),
    ]
