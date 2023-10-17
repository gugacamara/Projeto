# Generated by Django 4.2.6 on 2023-10-17 18:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroCliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('descricao', models.TextField()),
                ('valor', models.FloatField()),
                ('recebimento', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]