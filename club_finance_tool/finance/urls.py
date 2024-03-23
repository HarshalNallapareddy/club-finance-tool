from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from .views import *

from . import views
    

urlpatterns = [
    path('general_user/', views.general_user_view, name='general_user'),
    path('member/', views.member_view, name='member'),
    path('manager/', views.manager_view, name='manager'),
    path('institution/', views.institution_view, name='institution'),
    path('member/payment/', views.user_payment, name='payment')
]