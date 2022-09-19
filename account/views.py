from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login
from .service import *
from django.contrib.auth.forms import PasswordChangeForm
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
        taikhoan = request.POST.getlist('taikhoan')
        taikhoan = taikhoan[0]
        matkhau = request.POST.getlist('matkhau')
        matkhau = matkhau[0]
        nhaplaimatkhau = request.POST.getlist('nhaplaimatkhau')
        nhaplaimatkhau = nhaplaimatkhau[0]
        email = request.POST.getlist('email')
        email = email[0]
        sodienthoai = request.POST.getlist('sodienthoai')
        sodienthoai = sodienthoai[0]
        diachi = request.POST.getlist('diachi')
        diachi = diachi[0]
        thongBaoTrangThaiDangKy = checkDangKy(taikhoan, matkhau, nhaplaimatkhau, email, sodienthoai)
        msg=thongBaoTrangThaiDangKy
        if thongBaoTrangThaiDangKy == "Bạn đã đăng ký thành công":
            sql_DangKy(taikhoan, matkhau, email, sodienthoai, diachi)
    return render(request,'dangky.html', {'msg': msg})
def viewDangNhap(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee')
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
    form = PasswordChangeForm(request.user, request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            msg = 'Đổi mật khẩu thành công'
        else:
            msg = 'Đổi mật khẩu thất bại'
    return render(request, 'doimatkhau.html', {'form': form,'msg': msg})
def admin(request):
    return render(request,'admin.html')
def customer(request):
    return render(request,'customer.html')
def employee(request):
    return render(request,'employee.html')