import json
from datetime import timezone

from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View

from common import md5_
from .models import TSysUser, TSysRole, TSlidesshow, TLuckyTicket,THouseVerify,TPublicNotice



# Create your views here.
def login(request):
    # 分两种用户，一个是会员，一个管理员（系统）
    print('--->', request.method)
    if request.method == 'POST':
        print(request.POST)

        error = None

        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        remeber = request.POST.get('remeber', '')  # checkbox

        password_ = md5_.hash_encode(password)  # 转成md5后的密文
        print(password_)
        # 验证用户名和口令是否为空
        if not all((username, password)):
            error = f'用户名或口令不能为空！'

        login_user = TSysUser.objects.filter(username=username, password=password_).first()
        if login_user:
            # 系统管理员
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
            # login_user = TUser.objects.filter(name=username, auth_string=password).first()
            # if login_user:
            #     # 会员
            #     login_info = {
            #         '_id': login_user.user_id,
            #         'name': login_user.name,
            #         'code': '',
            #         'head': login_user.head,
            #         'email': login_user.mail,
            #         'phone': login_user.phone
            #     }
            # else:
            error = f'{username} 用户名或口令错误！'

        if not error:
            request.session['login_user'] = login_info
            return redirect('/')

    return render(request, 'login.html', locals())


def logout(request):
    del request.session['login_user']
    return redirect('/login/')


def index(request):
    return render(request, 'dashboard.html')


def role(request):
    action = request.GET.get('action', '')
    if action == 'del':
        TSysRole.objects.get(pk=request.GET.get('role_id')).delete()

    roles = TSysRole.objects.all()
    return render(request, 'role/list.html', locals())


def list_sys_user(request):
    action = request.GET.get('action', '')
    if action == 'del':
        TSysUser.objects.get(pk=request.GET.get('id_')).delete()

    # 查询系统时，除去超级管理员的用户
    users = TSysUser.objects.filter(~Q(pk=request.session['login_user']['_id'])).all()
    return render(request, 'sys_user/list.html', locals())


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

