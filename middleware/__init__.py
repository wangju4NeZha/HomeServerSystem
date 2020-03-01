#!/usr/bin/python3
# coding: utf-8
from django.http import HttpRequest
from django.shortcuts import redirect
<<<<<<< HEAD
=======
from django.urls import reverse
>>>>>>> 878b70e9a2d0381ca4f8ea0dfc7c016c12bdd579
from django.utils.deprecation import MiddlewareMixin


class LoginMiddleware(MiddlewareMixin):

    no_filter_path = (
        '/login/',
        '/logout/'
<<<<<<< HEAD
        '/regist/'
=======
>>>>>>> 878b70e9a2d0381ca4f8ea0dfc7c016c12bdd579
    )

    def process_request(self, request: HttpRequest):
        if request.path not in self.no_filter_path:
            # 验证当前会话是否已登录
            if not request.session.get('login_user', None):
<<<<<<< HEAD
                return redirect('/login/')
=======
                return redirect(reverse('main:login'))
>>>>>>> 878b70e9a2d0381ca4f8ea0dfc7c016c12bdd579


