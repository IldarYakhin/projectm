# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import random

from django.db import models


class License(models.Model):
    idlicense = models.AutoField(db_column='idLICENSE', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', unique=True, max_length=10, blank=True,
                            null=True)  # Field name made lowercase.
    activated = models.DateTimeField(db_column='ACTIVATED', blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(db_column='DURATION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'LICENSE'

    def get_list_of_existed_licenses(self):
        """
        :return: list of codes from db
        """
        pass

    def generator(qty, duration):  # 10 chars from ABCEFGHKLMNPRSTUVWXYZ23456789
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


    def get_id_by_code(code):
        """
        get License code and return idLicense
        :return:
        """
        pass

    def increase_duration(pk):
        """
        get License № and period in days
        like in example and increase duration on this days

        ABCEFGHKLMNPRSTUVWXYZ23456789 10
        ABCEFGHKLMNPRSTUVWXYZ23456789 5
        ABCEFGHKLMNPRSTUVWXYZ23456789 90
        etc

        :return:
        idLicense --> duration + days
        """

        pk = pk
        pass


class tools_for_license(models.Model):
    pass

# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)
#
#
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class User(models.Model):
#     password = models.CharField(max_length=128)
#     # last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     # first_name = models.CharField(max_length=150)
#     # last_name = models.CharField(max_length=150)
#     # email = models.CharField(max_length=254)
#     # is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     # date_joined = models.DateTimeField()
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.args = args
#         self.kwargs = kwargs


# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)
#
#
# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
#
# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_session'
