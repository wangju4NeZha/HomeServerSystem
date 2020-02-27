from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('role/', views.role),
    path('list_sysuser/', views.list_sys_user),
    path('edit_slide/', views.EditSlideWhowView.as_view()),
    path('list_sildeshow/', views.list_slide_show),
    path('list_houseverify/', views.AuditMessage.as_view()),
    path('list_publicnotice/', views.TPublic.as_view()),
    path('public_show/', views.TPublic.as_view()),

    path('lucky_ticket/', views.list_lucky),
    path('edit_lucky/', views.EditLuckyView.as_view()),
    path('', views.index)
]
