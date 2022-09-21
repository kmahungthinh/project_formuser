from django.urls import path
from . import views
from .service import *
urlpatterns = [
    path('', views.index, name= 'index'),
    path('dangnhap/', views.viewDangNhap, name='path_dangnhap'),
    path('dangky/', views.viewDangKy, name='path_dangky'),
    path('quenmatkhau/', views.viewQuenMatKhau, name='path_quenmatkhau'),
    path('khachhang/', views.viewKhachHang, name='path_khachhang'),
    path('nhanvien/', views.viewNhanVien, name='path_nhanvien'),
    path('doimatkhau/', views.viewDoiMatKhau, name='path_doimatkhau'),
    path('themkhachhang/', views.viewThemKhachHang, name='path_themkhachhang'),
    path('hienthidanhsachkhachhang/', views.hienThiDanhSachKhachHang, name='path_hienthidanhsachkhachhang'),
    path('delete/<int:id>', views.xoaKhachHang),

]