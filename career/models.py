from django.db import models


class Mineral(models.Model):
    iron_content = models.PositiveSmallIntegerField(
        verbose_name='Содержание железа Fe')
    silicon_content = models.PositiveSmallIntegerField(
        verbose_name='Содержание оксида кремния SiO2')

    class Meta:
        verbose_name = 'руда'
        verbose_name_plural = 'руды'

    def __str__(self):
        return f'Fe={self.iron_content}%, SiO2={self.silicon_content}%'


class Coordinate(models.Model):
    x_coordinate = models.IntegerField(
        verbose_name='Координата x')
    y_coordinate = models.IntegerField(
        verbose_name='Координата y')

    class Meta:
        verbose_name = 'координата'
        verbose_name_plural = 'координаты'

    def __str__(self):
        return f'({self.x_coordinate}, {self.y_coordinate})'


class Warehouse(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название склада')
    mineral = models.ManyToManyField(Mineral, related_name='warehouse',
                                     through='WarehouseMineral',
                                     through_fields=('warehouse', 'mineral'),
                                     verbose_name='Руда на складе')
    polygon_coord = models.ManyToManyField(Coordinate,
                                           related_name='warehouse',
                                           verbose_name='Координаты полигона')
    # x_coordinate = models.IntegerField(
    #     verbose_name='Координата склада x')
    # y_coordinate = models.IntegerField(
    #     verbose_name='Координата склада y')

    class Meta:
        verbose_name = 'склад'
        verbose_name_plural = 'склады'

    def __str__(self):
        return self.title


class DumpTruck(models.Model):
    number = models.CharField(max_length=50,
                              verbose_name='Бортовой номер самосвала')
    model = models.CharField(max_length=100,
                             verbose_name='Модель самосвала')
    carrying = models.PositiveIntegerField(
        verbose_name='Максимальная грузоподъемность, т')
    mineral = models.ManyToManyField(Mineral, related_name='dump_truck',
                                     through='DumpTruckMineral',
                                     through_fields=('dump_truck', 'mineral'),
                                     verbose_name='Руда в самосвале')
    warehouse = models.ManyToManyField(Warehouse, related_name='dump_truck',
                                       verbose_name='Склад для разгрузки')

    class Meta:
        verbose_name = 'самосвал'
        verbose_name_plural = 'самосвалы'

    def __str__(self):
        return self.number


class DumpTruckMineral(models.Model):
    weight = models.PositiveIntegerField(
        verbose_name='Масса руды, т')
    dump_truck = models.ForeignKey(DumpTruck, on_delete=models.CASCADE,
                                   related_name='mineral_weight_dumptruсk',
                                   verbose_name='Самосвал')
    mineral = models.ForeignKey(
        Mineral, on_delete=models.CASCADE,
        related_name='mineral_weight_dumptruсk',
        verbose_name='Руда')

    class Meta:
        verbose_name = 'масса руды в самосвале'
        verbose_name_plural = 'масса руды в самосвалах'

    def __str__(self):
        return f'{self.dump_truck.model}{self.dump_truck}, Руда:{self.mineral}'


class WarehouseMineral(models.Model):
    weight = models.PositiveIntegerField(
        verbose_name='Масса руды, т')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE,
                                  related_name='mineral_weight_warehouse',
                                  verbose_name='Склад')
    mineral = models.ForeignKey(
        Mineral, on_delete=models.CASCADE,
        related_name='mineral_weight_warehouse',
        verbose_name='Руда')

    class Meta:
        verbose_name = 'масса руды на складе'
        verbose_name_plural = 'масса руды на складах'

    def __str__(self):
        return f'{self.warehouse}, Руда:{self.mineral}'
