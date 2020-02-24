#!/usr/bin/python3
# coding: utf-8

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
            }
        }


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
