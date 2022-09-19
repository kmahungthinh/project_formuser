from django.urls import path
from . import views
from .service import *
urlpatterns = [
    path('', views.index, name= 'index'),
    path('dangnhap/', views.viewDangNhap, name='path_dangnhap'),
    path('dangky/', views.viewDangKy, name='path_dangky'),
    path('quenmatkhau/', views.viewQuenMatKhau, name='path_quenmatkhau'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('employee/', views.employee, name='employee'),
    path('doimatkhau/', views.viewDoiMatKhau, name='path_doimatkhau'),

]