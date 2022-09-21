from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login
from .service import *
from .models import *
from django.contrib.auth import update_session_auth_hash
# Create your views here.


def index(request):
    if request.method == 'POST' and 'dangnhap' in request.POST:
        return redirect('path_dangnhap')
    if request.method == 'POST' and 'dangky' in request.POST:
        return redirect('path_dangky')
    return render(request, 'index.html')


def viewDangKy(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'Đăng ký thành công'
            return render(request,'dangky.html', {'form': form, 'msg': msg})
    else:
        form = SignUpForm()
    return render(request,'dangky.html', {'form': form, 'msg': msg})
def viewDangNhap(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.la_khachhang:
                login(request, user)
                return redirect('path_khachhang')
            elif user is not None and user.la_nhanvien:
                login(request, user)
                return redirect('path_nhanvien')
            else:
                msg= 'Thông tin không hợp lệ'
        else:
            msg = 'Form đăng nhập không hợp lệ'
    return render(request, 'dangnhap.html', {'form': form, 'msg': msg})
def viewQuenMatKhau(request):
    msg = None
    if request.method == 'POST':
        email = request.POST.getlist('email')
        email = email[0]
        if emailCoAcong(email):
            print(email)
            return redirect('path_dangnhap')
        else:
            msg = 'Email không hợp lệ'
    return render(request, 'quenmatkhau.html', {'msg': msg})
def viewDoiMatKhau(request):
    msg = None
    if str(request.user) == 'AnonymousUser':
        print("thoa man")
        return redirect('path_dangnhap')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            msg = 'Đổi mật khẩu thành công'
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'doimatkhau.html', {'form': form, 'msg': msg, 'nguoidung':str(request.user)})
def admin(request):
    return render(request,'admin.html')
def viewKhachHang(request):
    return render(request,'khachhang.html')
def viewNhanVien(request):
    return render(request,'nhanvien.html')
def viewThemKhachHang(request):
    msg = None
    if request.method == 'POST':
        form = KhachHangForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'Thêm thành công'
            return render(request, 'khachhang/them.html', {'form': form, 'msg': msg})
    else:
        print("K Hợp lệ")
        form = KhachHangForm()
    return render(request, 'khachhang/them.html', {'form': form, 'msg': msg})
def hienThiDanhSachKhachHang(request):
    khachhang = User.objects.filter(la_khachhang=1)
    return render(request,"khachhang/hienthi.html",{'khachhang':khachhang})
def suaKhachHang(request, id):
    employee = User.objects.get(la_khachhang=True)
    return render(request,'sua.html', {'employee':employee})
def xoaKhachHang(request, id):
    khachhang = User.objects.filter(id=id)
    khachhang.delete()
    khachhang = User.objects.filter(la_khachhang=1)
    return redirect("/hienthidanhsachkhachhang")

