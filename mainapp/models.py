# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class License(models.Model):
    """
    TODO:
    В админке сделать
    Пользователь хочет видеть следующие статистические сводки:
    – Общее количество лицензий
    – Количество активированных лицензий
    – Количество неактивированных лицензий
    – Количество просроченных лицензий
    – Гистограмму распределения длительности лицензий
    """
    idlicense = models.AutoField(db_column='idLICENSE', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', unique=True, max_length=10, blank=True,
                            null=True)  # Field name made lowercase.
    activated = models.DateTimeField(db_column='ACTIVATED', blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(db_column='DURATION', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        result = f'{self.code} {self.duration}'
        return result

    class Meta:
        db_table = 'LICENSE'






