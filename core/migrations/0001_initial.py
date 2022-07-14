# Generated by Django 4.0.5 on 2022-07-14 22:08

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, verbose_name='Id de Categoria')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='nombre')),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaAnimal',
            fields=[
                ('idCategoriaA', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Categoria')),
                ('nombreCategoriaA', models.CharField(max_length=50, verbose_name='Nombre de Categoria Animal')),
            ],
        ),
        migrations.CreateModel(
            name='SexoCliente',
            fields=[
                ('idsexo', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de sexo')),
                ('nombreSexo', models.CharField(max_length=50, verbose_name='Nombre de sexo')),
            ],
        ),
        migrations.CreateModel(
            name='Productos_Animal',
            fields=[
                ('id_producto', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='id_producto')),
                ('descripcionP', models.CharField(max_length=60, verbose_name='Descripcion')),
                ('marca', models.CharField(max_length=20, verbose_name='Marca')),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoriaanimal', verbose_name='Categoria Animal')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='codigo')),
                ('nombre', models.CharField(max_length=250, verbose_name='nombre')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='nombre')),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('marca', models.CharField(max_length=20, verbose_name='Marca')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precio', models.PositiveIntegerField()),
                ('destacado', models.BooleanField(default=True)),
                ('activo', models.BooleanField(default=True)),
                ('estado', models.CharField(max_length=20, verbose_name='Estado')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria', verbose_name='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('rut_cliente', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='rut_cliente')),
                ('nombres_cliente', models.CharField(max_length=30, verbose_name='Nombres')),
                ('apellidos_clientes', models.CharField(max_length=30, verbose_name='Apellidos')),
                ('correos_clientes', models.CharField(max_length=30, verbose_name='Correos')),
                ('dirreciones_clientes', models.CharField(max_length=30, verbose_name='Dirreción')),
                ('num_cel_clientes', models.CharField(max_length=30, verbose_name='Número de celular')),
                ('sexo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sexocliente', verbose_name='Sexo cliente')),
            ],
        ),
    ]
