import json

from django.core.serializers import serialize
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from common import md5_
from .models import TSysRole, TSysUser, TPublicNotice, TSlidesshow, TLuckyTicket, THouseVerify


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
        print(password_)

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
    notices = TPublicNotice.objects.filter(public_status=1)
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
    return render(request, 'role/list.html', locals())   #


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


class EditRoleView(View):    # 编辑角色信息
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


class EditPublicNotice(View):   # 编辑公告
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


def list_slide_show(request):
    action = request.GET.get('action', '')
    if action == 'del':
        TSlidesshow.objects.get(pk=request.GET.get('id_')).delete()
    slides = TSlidesshow.objects.all()
    return render(request, 'sys_user/list_sildeshow.html', locals())


class EditSlideWhowView(View):
    def get(self, request):
        id_ = request.GET.get('id_', '')
        if id_:
            obj = TSlidesshow.objects.get(pk=id_)

        return render(request, 'sys_user/edit_slide.html', locals())

    def post(self, request):
        from .forms import SlideForm
        id_ = request.POST.get('id', '')
        if id_:
            form = SlideForm(request.POST, instance=TSlidesshow.objects.get(pk=id_))
        else:
            form = SlideForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/list_sildeshow/')

        errors = json.loads(form.errors.as_json())

        return render(request, 'sys_user/edit_slide.html', locals())


def list_lucky(request):
    action = request.GET.get('action', '')
    if action == 'del':
        TLuckyTicket.objects.get(pk=request.GET.get('id_')).delete()
    tickets = TLuckyTicket.objects.all()
    return render(request, 'sys_user/list_lucky.html', locals())


class EditLuckyView(View):
    def get(self, request):
        id_ = request.GET.get('id_', '')
        if id_:
            obj = TLuckyTicket.objects.get(pk=id_)

        return render(request, 'sys_user/edit_lucky.html', locals())

    def post(self, request):
        from .forms import LuckyForm
        id_ = request.POST.get('id', '')
        begin = request.POST.get('begin_time')
        print(f'------->>>{begin}---{type(begin)}')
        if id_:
            form = LuckyForm(request.POST, instance=TLuckyTicket.objects.get(pk=id_))
        else:
            form = LuckyForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/lucky_ticket/')

        errors = json.loads(form.errors.as_json())

        return render(request, 'sys_user/edit_lucky.html', locals())


class AuditMessage(View):
    def get(self, request):
        action = request.GET.get('action', '')
        if action:
            obj = THouseVerify.objects.get(pk=request.GET.get('id_'))

            if action == 'yes':
                obj.verify_status = 1
            elif action == 'no':
                obj.verify_status = 2
                obj.remarks = request.GET.get('remarks', '')
            obj.save()
            obj.full_clean()


        objs = THouseVerify.objects.filter(verify_status=0).all()
        return render(request, 'message/list_audit.html', locals())


class TPublic(View):
    def get(self, request):
        action = request.GET.get('action', '')
        public_status = request.GET.get('public_status','')
        if action:
            obj = TPublicNotice.objects.get(pk=request.GET.get('id_'))
            if action == 'yes':
                obj.public_status = 1
            elif action == 'no':
                obj.public_status = 2
                obj.remarks = request.GET.get(' public_remarks', '')
            obj.save()
            obj.full_clean()

        if public_status:
            objs = TPublicNotice.objects.filter(public_status=1).all()
        else:
            objs = TPublicNotice.objects.filter(public_status=0).all()
        return render(request, 'message/list_public.html', locals())


from mainapp.models import TComplaint
def get_complain(request):
    # get请求参数：action 有三个可选值（yes, del, query)
    # yes和del 都有一个额外参数：id_(投诉的ID）
    # query 有一个参数wd:可以按照订单号或者用户账号、手机号搜索都行
    action = request.GET.get('action', '')
    if action=='yes':
        obj = TComplaint.objects.get(pk=request.GET.get('id_'))
        obj.state = 1
        obj.save()
        obj.full_clean()
    if action=='del':
        TComplaint.objects.get(pk=request.GET.get('id_')).delete()
    # 查看评论主页
    complains = TComplaint.objects.all()
    return render(request, 'complaint/list.html', locals())


from mainapp.models import TComment
def get_comment(request):

    # get请求参数：action 有三个可选值（yes, del, query)
    # yes和del 都有一个额外参数：id_(投诉的ID）
    # query 有一个参数wd:可以按照订单号或者用户账号、手机号搜索都行
    action = request.GET.get('action', '')
    if action == 'yes':
        obj = TComment.objects.get(pk=request.GET.get('id_'))
        obj.state = 1
        obj.save()
        obj.full_clean()
    if action == 'del':
        TComment.objects.get(pk=request.GET.get('id_')).delete()
    comments = TComment.objects.all()
    return render(request, 'comment/list.html', locals())
