# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import random

from django.contrib import admin
from django.db import models
from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect


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


    def generator(request, qty, duration):  # 10 chars from ABCEFGHKLMNPRSTUVWXYZ23456789
        """
        get needed qty of Licenses and
        :return:
        dict {'License': duration}
        """
        chars = 'ABCEFGHKLMNPRSTUVWXYZ23456789'
        counter = qty
        output = {}
        while counter >= 0:
            example = ''.join(random.sample(chars, len(chars)))
            if License.objects.filter(code=example).exists():
                continue
            else:
                output[example] = duration
                counter -= 1
        return output



    def increase_duration(pk):
        """
        get License № and period in days
        like in example and increase duration on this days

        ABCEFGHKLM 10
        ABCEFGHKLM 5
        ABCEFGHKLM 90
        etc
        :return:
        idLicense --> duration + days
        """

        pass








