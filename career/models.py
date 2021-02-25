from django.db import models


class Mineral(models.Model):
    weight = models.PositiveIntegerField(
        verbose_name='Масса руды')
    iron_content = models.PositiveSmallIntegerField(
        verbose_name='Содержание железа Fe')
    silicon_content = models.PositiveSmallIntegerField(
        verbose_name='Содержание оксида кремния SiO2')

    class Meta:
        verbose_name = 'руда'
        verbose_name_plural = 'руды'


class DumpTruck(models.Model):
    number = models.CharField(max_length=50,
                              verbose_name='Бортовой номер самосвала')
    model = models.CharField(max_length=100,
                             verbose_name='Модель самосвала')
    carrying = models.PositiveIntegerField(
        verbose_name='Максимальная грузоподъемность')
    mineral = models.ForeignKey(Mineral, on_delete=models.CASCADE,
                                related_name='dump_truck',
                                verbose_name='Руда в самосвале')

    class Meta:
        verbose_name = 'самосвал'
        verbose_name_plural = 'самосвалы'

    def __str__(self):
        return self.number


class Coordinate(models.Model):
    x_coordinate = models.IntegerField(
        verbose_name='Координата x')
    y_coordinate = models.IntegerField(
        verbose_name='Координата y')

    class Meta:
        verbose_name = 'координата'
        verbose_name_plural = 'координаты'


class Warehouse(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название склада')
    mineral = models.ForeignKey(Mineral, on_delete=models.CASCADE,
                                related_name='warehouse',
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
