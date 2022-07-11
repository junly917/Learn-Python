import re

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings


class MyMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        current_path = request.path_info
        user_status = request.session.get('user_info', [])
        flag = False
        url_list = request.session.get("permission", [])
        for w_list in settings.WHITE_URL_LIST:
            res = re.match("^" + w_list + "$", current_path)
            print(("^" + w_list + "$", current_path))
            if res:
                print('在白名单内')
                flag = True
                return None
            else:
                print("w_list:", w_list)

        # if not user_status:
        #     print("未登录")
        #     return redirect("/login/")
        if not flag:
            for item in url_list:
                res = re.match("^" + item['url'] + "$", current_path)
                print(res)
                # res = re.match('^' + current_path + '$', item['url'])
                if res:
                    return True
            print("Access Deny")
            return HttpResponse("Access Deny")
