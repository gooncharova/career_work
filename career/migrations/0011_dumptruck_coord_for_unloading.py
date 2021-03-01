# Generated by Django 3.1.5 on 2021-02-28 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0010_auto_20210228_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='dumptruck',
            name='coord_for_unloading',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='unloading', to='career.coordinate', verbose_name='Координаты для разгрузки'),
            preserve_default=False,
        ),
    ]