# Generated by Django 4.2 on 2024-02-06 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_alter_clientes_cliente_telefono'),
    ]

    operations = [
        migrations.CreateModel(
            name='clienteRUC20',
            fields=[
                ('clientes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='clientes.clientes')),
                ('Nombre_Empresa', models.CharField(max_length=100)),
            ],
            bases=('clientes.clientes',),
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='Cliente_Apellido',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='Cliente_Nombre',
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='Tipo_Ruc',
        ),
        migrations.AlterField(
            model_name='clientes',
            name='Cliente_telefono',
            field=models.CharField(max_length=9),
        ),
        migrations.CreateModel(
            name='clienteRUC10',
            fields=[
                ('clientes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='clientes.clientes')),
                ('Cliente_Nombre', models.CharField(max_length=100)),
                ('Cliente_Apellido', models.CharField(max_length=100)),
            ],
            bases=('clientes.clientes',),
        ),
    ]