# Generated by Django 3.1.5 on 2021-02-25 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_coordinate', models.IntegerField(verbose_name='Координата x')),
                ('y_coordinate', models.IntegerField(verbose_name='Координата y')),
            ],
            options={
                'verbose_name': 'координата',
                'verbose_name_plural': 'координаты',
            },
        ),
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.PositiveIntegerField(verbose_name='Масса руды')),
                ('iron_content', models.PositiveSmallIntegerField(verbose_name='Содержание железа Fe')),
                ('silicon_content', models.PositiveSmallIntegerField(verbose_name='Содержание оксида кремния SiO2')),
            ],
            options={
                'verbose_name': 'руда',
                'verbose_name_plural': 'руды',
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название склада')),
                ('mineral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse', to='career.mineral', verbose_name='Руда на складе')),
                ('polygon_coord', models.ManyToManyField(related_name='warehouse', to='career.Coordinate', verbose_name='Координаты полигона')),
            ],
            options={
                'verbose_name': 'склад',
                'verbose_name_plural': 'склады',
            },
        ),
        migrations.CreateModel(
            name='DumpTruck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50, verbose_name='Бортовой номер самосвала')),
                ('model', models.CharField(max_length=100, verbose_name='Модель самосвала')),
                ('carrying', models.PositiveIntegerField(verbose_name='Максимальная грузоподъемность')),
                ('mineral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dump_truck', to='career.mineral', verbose_name='Руда в самосвале')),
            ],
            options={
                'verbose_name': 'самосвал',
                'verbose_name_plural': 'самосвалы',
            },
        ),
    ]