from django.contrib import admin

from .models import Permissions, PermissionGroup, Users, Role


class PermissionsAdmin(admin.ModelAdmin):    #定义ZoneAdmin管理类
    list_display = ('name','url','icon', 'group_menu', 'group')   #在管理后台显示的内容
    list_display_links = (['name'])   #单击哪些内容可编辑


class RoleAdmin(admin.ModelAdmin):    #定义ZoneAdmin管理类
    list_display = ('name',)   #在管理后台显示的内容
    list_display_links = (['name'])   #单击哪些内容可编辑


class UsersAdmin(admin.ModelAdmin):    #定义ZoneAdmin管理类
    list_display = ('username','password','mobile')   #在管理后台显示的内容
    list_display_links = (['username'])   #单击哪些内容可编辑


class PermissionGroupAdmin(admin.ModelAdmin):    #定义ZoneAdmin管理类
    list_display = ('name',)   #在管理后台显示的内容
    list_display_links = ('name',)   #单击哪些内容可编辑



admin.site.register(Permissions,PermissionsAdmin)
admin.site.register(PermissionGroup,PermissionGroupAdmin)
admin.site.register(Role,RoleAdmin)
admin.site.register(Users,UsersAdmin)