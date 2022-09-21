from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from .models import User
import re
from .service import *

So="0123456789"
alphabetHoa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
class UserCreationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username",)

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    diachi = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    sodienthoai = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if len(password1)<8:
                raise forms.ValidationError("Độ dài mật khẩu tối thiểu phải là 8 ký tự")
            if thoaManKyTuQuyQuoc(password1)==False:
                raise forms.ValidationError\
                    ("Mật khẩu đăng ký không đúng định dạng (phải bao gồm: chữ hoa,chữ thường,số, ký tự đặc biệt")
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Mật khẩu không hợp lệ")
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','sodienthoai','diachi')
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class SetPasswordForm(forms.Form):
    new_password1 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    new_password2 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SetPasswordForm, self).__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if len(password1) < 8:
                raise forms.ValidationError("Độ dài mật khẩu tối thiểu phải là 8 ký tự")
            elif thoaManKyTuQuyQuoc(password1) == False:
                raise forms.ValidationError\
                    ("Mật khẩu mới không đúng định dạng (phải bao gồm: chữ hoa,chữ thường,số, ký tự đặc biệt")
            elif password1 != password2:
                raise forms.ValidationError("Mật khẩu không khớp")
        return password2

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])
        if commit:
            self.user.save()
        return self.user

class PasswordChangeForm(SetPasswordForm):

    old_password = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    def clean_old_password(self):
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError("Mật khẩu cũ không đúng")
        return old_password
class KhachHangForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password1=forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    makhachhang = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    diachi = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    sodienthoai = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    madinhdanh=forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    motanoidungyeucau = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    giatien = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    soluongkhaosat = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    socaukhaosat = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username','password1','makhachhang','last_name','diachi','sodienthoai','madinhdanh', 'email', 'motanoidungyeucau', 'giatien','soluongkhaosat','socaukhaosat','la_khachhang')
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.la_khachhang = True
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
