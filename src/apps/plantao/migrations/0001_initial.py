# Generated by Django 2.2.5 on 2019-09-30 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('área', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Plantonista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('telefone', models.CharField(max_length=20, verbose_name='Contato')),
                ('observação', models.CharField(max_length=40, verbose_name='Observação')),
                ('área', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantao.Area')),
            ],
        ),
    ]
