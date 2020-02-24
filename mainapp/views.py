import json

from django.core.serializers import serialize
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from common import md5_
from .models import TSysRole, TSysUser, TPublicNotice


# Create your views here.
def login(request):
    # 分两种用户，一个是会员，一个管理员（系统）
    # print('--->', request.method)
    if request.method == 'POST':
        # print(request.POST)
        error = None

        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        remeber = request.POST.get('remeber', '')  # checkbox

        password_ = md5_.hash_encode(password)  # 转成md5后的密文

        # 验证用户名和口令是否为空
        if not all((username, password)):
            error = f'用户名或口令不能为空！'
        else:
            login_user = TSysUser.objects.filter(username=username, password=password_).first()
            if login_user:
                # 超级管理员
                role_ = login_user.role

                login_info = {
                    'user_id': login_user.user_id,
                    'head': str(login_user.head),
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
    notices = TPublicNotice.objects.filter(~Q(state=1))
    return render(request, 'dashboard.html', locals())


def role(request):
    """
    查看角色页面和删除角色
    :param request:
    :return:
    """
    action = request.GET.get('action', '')
    if action == 'del':
        role_id = request.GET.get('role_id')
        TSysRole.objects.get(role_id=role_id).delete()
        user_list = TSysUser.objects.filter(role_id=role_id)
        for obj in user_list:
            obj.delete()

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
        TSysUser.objects.get(user_id=request.GET.get('user_id')).delete()

    # 查询系统时，除去超级管理员的用户
    users = TSysUser.objects.filter(~Q(user_id=request.session['login_user']['user_id'])).all()
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
        user_id = request.GET.get('user_id', '')
        if user_id:
            obj = TSysUser.objects.get(user_id=user_id)

        roles = TSysRole.objects.filter(~Q(role_code='admin'))
        return render(request, 'sys_user/edit.html', locals())

    def post(self, request):
        from .forms import SysUserForm
        # print(request.POST,"+++++++++++++++++++++")
        user_id = request.POST.get('user_id', '')
        if user_id:
            form = SysUserForm(request.POST, request.FILES, instance=TSysUser.objects.get(user_id=user_id))
        else:
            form = SysUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('main:list_sysuser'))

        errors = json.loads(form.errors.as_json())

        roles = TSysRole.objects.filter(~Q(code='admin'))

        return render(request, 'sys_user/edit.html', locals())


def logout(request):
    # 退出
    del request.session['login_user']
    return redirect(reverse("main:login"))


def notice(request):
    notices = TPublicNotice.objects.all()
    action = request.GET.get('action', '')
    if action:
        TPublicNotice.objects.get(public_notice_id=request.GET.get('public_notice_id')).delete()
    return render(request, 'notice/list.html', locals())


class EditPublicNotice(View):
    def get(self, request):
        public_notice_id = request.GET.get('public_notice_id', '')
        if public_notice_id:
            notice = TPublicNotice.objects.get(public_notice_id=public_notice_id)
        return render(request, 'notice/edit.html', locals())

    def post(self, request):
        from .forms import NoticeForm
        public_notice_id = request.POST.get('public_notice_id', '')
        if public_notice_id:
            notice = TPublicNotice.objects.get(public_notice_id=public_notice_id)
            form = NoticeForm(request.POST, instance=notice)
        else:
            form = NoticeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('main:notice'))

        errors = json.loads(form.errors.as_json())
        return render(request, 'notice/edit.html', locals())









def feedback(request):
    return HttpResponse('查看投诉信息')


def comment(request):
    return HttpResponse('查看评论信息')


