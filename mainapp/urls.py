from django.urls import path

from mainapp import views
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dash'),


    path('role/', views.role, name='role'),
    path('edit_role/', views.EditRoleView.as_view(), name='edit_role'),
    path('list_sysuser/', views.list_sys_user, name='list_sysuser'),
    path('edit_sysuser/', views.EditSysUserView.as_view(), name="edit_sysuser"),

    path('notice/', views.notice, name='notice'),
    path('edit_notice/', views.EditPublicNotice.as_view(), name='edit_notice'),

    path('edit_slide/', views.EditSlideWhowView.as_view()),
    path('list_sildeshow/', views.list_slide_show),
    path('list_houseverify/', views.AuditMessage.as_view()),
    path('list_publicnotice/', views.TPublic.as_view()),
    path('public_show/', views.TPublic.as_view()),

    path('lucky_ticket/', views.list_lucky),
    path('edit_lucky/', views.EditLuckyView.as_view()),

    path('complain/', views.get_complain, name='comp'),
    path('comment/', views.get_comment, name='cmmt'),


]

