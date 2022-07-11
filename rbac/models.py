from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    mobile = models.CharField(max_length=12, verbose_name='手机号')
    role = models.ManyToManyField('Role', verbose_name='角色', related_name='userTorole')

    class Meta:
        # db_name = 'tb_users'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}-{}".format(self.username, self.mobile)


class Role(models.Model):
    name = models.CharField(max_length=24, verbose_name='名称')
    permission = models.ManyToManyField('Permissions', verbose_name='权限', related_name='roleToperm')

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        # db_name = 'tb_roles'
        verbose_name = '角色表'
        verbose_name_plural = verbose_name


class Permissions(models.Model):
    name = models.CharField(max_length=24, verbose_name='名称')
    url = models.CharField(max_length=128, verbose_name='路径')
    icon = models.CharField(max_length=32, verbose_name='图标', blank=True, null=True)
    group = models.ForeignKey(verbose_name='所属权限组', to="PermissionGroup",
                              on_delete=models.CASCADE, null=True, blank=True)
    group_menu = models.ForeignKey(verbose_name='组内菜单', to="Permissions",
                                   null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '权限表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}-{}".format(self.name, self.url)


class PermissionGroup(models.Model):
    name = models.CharField(max_length=24, verbose_name='名称')

    def __str__(self):
        return self.name
    class Meta:
        # db_name = 'tb_permission'
        verbose_name = '权限组表'
        verbose_name_plural = verbose_name