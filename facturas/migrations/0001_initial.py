# Generated by Django 4.2 on 2023-09-10 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orden_de_trabajo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Numero_de_factura', models.IntegerField()),
                ('Fecha_Emision', models.DateField()),
                ('Id_cliente', models.CharField(max_length=12)),
                ('Importe', models.FloatField()),
                ('IGV', models.FloatField()),
                ('Detraccion', models.FloatField()),
                ('Pago_de_detraccion', models.BooleanField()),
                ('Documento_factura', models.FileField(upload_to='archivos/')),
                ('Orden_de_trabajo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orden_de_trabajo.orden_trabajo')),
            ],
        ),
    ]