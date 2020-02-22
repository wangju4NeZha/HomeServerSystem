import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from common import md5_
from .models import TSysRole, TSysUser


# Create your views here.
def login(request):
    # 分两种用户，一个是会员，一个管理员（系统）
    # print('--->', request.method)
    if request.method == 'POST':
        # print(request.POST)
        login_info = dict()
        error = None

        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        remeber = request.POST.get('remeber', '')  # checkbox

        password_ = md5_.hash_encode(password)  # 转成md5后的密文

        # 验证用户名和口令是否为空
        if not all((username, password)):
            error = f'用户名或口令不能为空！'

        if TSysUser.objects.filter(username=username, password=password_, role_id=1):
            # 超级管理员
            login_user = TSysUser.objects.filter(username=username, password=password_, role_id=1).first()
            role_ = TSysRole.objects.get(role_id=login_user.role_id)
            login_info = {
                'user_id': login_user.user_id,
                'head': login_user.head,
                'email': login_user.email,
                'nick_name': login_user.nick_name,
                'role_name': role_.role_name,
                'role_code': role_.role_code,
            }

        elif TSysUser.objects.filter(username=username, password=password_, role_id=2):
            login_user = TSysUser.objects.filter(username=username, password=password_, role_id=2).first()
            role_ = TSysRole.objects.get(role_id=login_user.role_id)
            login_info = {
                'user_id': login_user.user_id,
                'head': login_user.head,
                'email': login_user.email,
                'nick_name': login_user.nick_name,
                'role_name': role_.role_name,
                'role_code': role_.role_code,
            }
        else:
            error = f'{username} 用户名或口令错误！'

        if not error:
            request.session['login_user'] = login_info
            return redirect(reverse('main:dash'))

    return render(request, 'login.html', locals())


def dashboard(request):
    """
    登陆之后主页界面
    :param request:
    :return:
    """
    return render(request, 'dashboard.html')


def role(request):
    """
    查看角色页面和删除角色
    :param request:
    :return:
    """
    action = request.GET.get('action', '')
    if action == 'del':
        TSysRole.objects.get(pk=request.GET.get('role_id')).delete()
    roles = TSysRole.objects.all()
    return render(request, 'role/list.html', locals())


def list_sys_user(request):
    """
    查看所有管理员和删除管理员
    :param request:
    :return:
    """
    action = request.GET.get('action', '')
    if action == 'del':
        TSysUser.objects.get(pk=request.GET.get('id_')).delete()

    # 查询系统时，除去超级管理员的用户
    users = TSysUser.objects.filter(~Q(pk=request.session['login_user']['user_id'])).all()
    return render(request, 'sys_user/list.html', locals())


class EditRoleView(View):
    """
    编辑角色信息和增加角色信息
    """
    def get(self, request):
        role_id = request.GET.get('role_id', '')
        if role_id:
            role = TSysRole.objects.get(role_id=role_id)
        return render(request, 'role/edit.html', locals())

    def post(self, request):
        from .forms import RoleForm
        role_id = request.POST.get('role_id', '')
        if role_id:
            form = RoleForm(request.POST, instance=TSysRole.objects.get(role_id=role_id))
        else:
            form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('main:role'))

        errors = json.loads(form.errors.as_json())
        return render(request, 'role/edit.html', locals())


class EditSysUserView(View):
    """
    编辑管理员信息和增加管理员
    """
    def get(self, request):
        user_id = request.GET.get('id_', '')
        if user_id:
            obj = TSysUser.objects.get(user_id=user_id)

        roles = TSysRole.objects.filter(~Q(role_code='admin'))
        return render(request, 'sys_user/edit.html', locals())

    def post(self, request):
        from .forms import SysUserForm

        user_id = request.POST.get('user_id', '')
        if user_id:
            form = SysUserForm(request.POST, instance=TSysUser.objects.get(user_id=user_id))
        else:
            form = SysUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/list_sysuser/')

        errors = json.loads(form.errors.as_json())

        roles = TSysRole.objects.filter(~Q(code='admin'))

        return render(request, 'sys_user/edit.html', locals())


def logout(request):
    # 退出
    del request.session['login_user']
    return redirect(reverse("main:login"))


def notice(request):
    return HttpResponse('查看公告信息')


def feedback(request):
    return HttpResponse('查看投诉信息')


def comment(request):
    return HttpResponse('查看评论信息')
