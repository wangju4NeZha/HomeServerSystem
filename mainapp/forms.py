#!/usr/bin/python3
# coding: utf-8

<<<<<<< HEAD
from django import forms
from .models import TSysRole, TSysUser, TSlidesshow, TLuckyTicket


# class RoleForm(forms.ModelForm):    # 管理员角色
#
#     class Meta:
#         model = TSysRole
#         fields = ['name', 'code']  # '__all__'
#         error_messages = {
#             'name': {
#                 'required': '角色名不能为空'
#             },
#             'code': {
#                 'required': '角色代码不能为空'
#             }
#         }

# class SysUserForm(forms.ModelForm):   # 系统管理员
#
#     class Meta:
#         model = TSysUser
#         fields = ['username', 'auth_string', 'role_id', 'nick_name']  # '__all__'
#         error_messages = {
#             'username': {
#                 'required': '账号不能为空'
#             },
#             'auth_string': {
#                 'required': '口令不能为空'
#             },
#             'role_id': {
#                 'required': '系统用户角色不能为空'
#             }
#         }


class SlideForm(forms.ModelForm):     # 轮播图

    class Meta:
        model = TSlidesshow
        fields = ['house', 'ord']  # '__all__'
        error_messages = {
            'house': {
                'required': '房屋ID不能为空'
            },
            'ord': {
                'required': '顺序不能为空'
=======
"""
用来对数据进行检验

"""

from django import forms
from .models import TSysRole, TSysUser, TPublicNotice


class RoleForm(forms.ModelForm):

    class Meta:
        model = TSysRole
        fields = ['role_name', 'role_code']  # '__all__'
        error_messages = {
            'role_name': {
                'required': '角色名不能为空'
            },
            'role_code': {
                'required': '角色代码不能为空'
            }
        }

class SysUserForm(forms.ModelForm):

    class Meta:
        model = TSysUser
        fields = ['username', 'password', 'role_id', 'nick_name', 'head']
        error_messages = {
            'username': {
                'required': '账号不能为空'
            },
            'nick_name': {
                'required': '昵称不能为空'
            },
            'password': {
                'required': '口令不能为空'
            },
            'role_id': {
                'required': '系统用户角色不能为空'
>>>>>>> 878b70e9a2d0381ca4f8ea0dfc7c016c12bdd579
            }
        }


<<<<<<< HEAD
class LuckyForm(forms.ModelForm):   # 代金券

    class Meta:
        model = TLuckyTicket
        fields = ['money', 'begin_time', 'end_time', 'image']  # '__all__'
        error_messages = {
            'money': {
                'required': '面值不能为空'
            },
            'begin_time': {
                'required': '起始时间不能为空'
            },
            'end_time': {
                'required': '结束时间不能为空'
            },
            'image': {
                'required': '图片路径不能为空'
            }
        }
=======
class NoticeForm(forms.ModelForm):

    class Meta:
        model = TPublicNotice
        fields = ['content', 'title', 'public_time', 'note', 'link_url', 'public_notice_id']
        error_messages = {
            'title': {
                'required': '标题不能为空'
            },
            'link_url': {
                'required': '外部连接不能为空'
            },
            'content':{
                'required': '内容不能为空'
            }
        }
>>>>>>> 878b70e9a2d0381ca4f8ea0dfc7c016c12bdd579
