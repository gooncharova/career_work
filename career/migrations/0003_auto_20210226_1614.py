# Generated by Django 3.1.5 on 2021-02-26 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0002_auto_20210226_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dumptruckmineral',
            name='dump_truck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mineral_weight', to='career.dumptruck', verbose_name='Самосвал'),
        ),
        migrations.AlterField(
            model_name='dumptruckmineral',
            name='mineral',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mineral_weight', to='career.mineral', verbose_name='Масса руды, т'),
        ),
    ]
