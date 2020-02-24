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

    path('feedback/', views.feedback, name='fed'),
    path('comment/', views.comment, name='com'),
]


