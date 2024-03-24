from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView, LoginView
from .views import *

from . import views
    

urlpatterns = [
    path('general_user/', views.general_user, name='general_user'),
    path('member/', views.member_view, name='member'),
    path('manager/', views.manager_view, name='manager'),
    path('institution/', views.institution_view, name='institution'),
    path('member/payment/', views.user_payment, name='payment'),
    path('login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path("signup/", SignUpView.as_view(template_name='auth/register.html'), name="register"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('member/reimbursement/', views.reimbursement, name='reimbursement'),
    path('member/general_user/', views.general_user_view, name='general_user'),
]