# Generated by Django 5.0 on 2023-12-08 11:54

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oddział',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30)),
                ('ceo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Zmiana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stanowisko', models.CharField(max_length=30)),
                ('zakres_godzin', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Dziecko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pensja', models.FloatField()),
                ('st_anorekcji', models.CharField(max_length=30)),
                ('kolor', models.CharField(max_length=20)),
                ('choroby', models.CharField(max_length=200)),
                ('wiek', models.IntegerField(validators=[django.core.validators.MinValueValidator(4), django.core.validators.MaxValueValidator(14)])),
                ('oddział', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fabryka.oddział')),
                ('zmiana', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fabryka.zmiana')),
            ],
        ),
    ]