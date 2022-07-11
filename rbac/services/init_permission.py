from django.http import request

from rbac.models import Permissions


def init_user(user_obj, request):
    rid = user_obj.role.first().id
    user_info = {
        'id': user_obj.id,
        'username': user_obj.username,
        'role_id': rid
    }
    permission_list = []
    [permission_list.append(x) for x in Permissions.objects.filter(roleToperm=rid).values("url")]

    menu_list = []
    for m in Permissions.objects.filter(group__isnull=False).filter(roleToperm=rid).values():
        menu_info = {
            "authName": m["name"], "id": m["id"], "url": m["url"],
            "icon": m["icon"],
            "level": m["group_menu_id"] if m["group_menu_id"] is not None else 0
        }
        menu_list.append(menu_info)
    print("menu_list:", menu_list)
    request.session["user_info"] = user_info
    request.session["permission"] = permission_list
    request.session["menu_list"] = menu_list
    return request