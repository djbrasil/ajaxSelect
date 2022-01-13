# Generated by Django 3.2.9 on 2022-01-13 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124)),
                ('text', models.TextField()),
                ('empresas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitacao', to='end.empresas')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('c_cep', models.CharField(max_length=10)),
                ('c_road', models.CharField(max_length=200)),
                ('c_district', models.CharField(max_length=200)),
                ('c_complement', models.CharField(max_length=30)),
                ('c_number', models.CharField(max_length=5)),
                ('c_city', models.CharField(max_length=20)),
                ('c_uf', models.CharField(max_length=2)),
                ('empresas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endereco', to='end.empresas')),
            ],
        ),
    ]