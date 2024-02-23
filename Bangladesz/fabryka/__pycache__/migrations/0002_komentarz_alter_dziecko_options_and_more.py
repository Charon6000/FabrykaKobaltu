# Generated by Django 5.0 on 2024-02-16 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabryka', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Komentarz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tresc', models.CharField(max_length=200)),
                ('ocena', models.IntegerField()),
                ('data', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Komentarze',
            },
        ),
        migrations.AlterModelOptions(
            name='dziecko',
            options={'verbose_name_plural': 'Dzieci'},
        ),
        migrations.AlterModelOptions(
            name='oddział',
            options={'verbose_name_plural': 'Oddziały'},
        ),
        migrations.AlterModelOptions(
            name='zmiana',
            options={'verbose_name_plural': 'Zmiany'},
        ),
    ]