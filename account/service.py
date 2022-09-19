import hashlib
from django.contrib.auth.models import User
from .models import *
def string_To_List_PhanTuTrongListLaString(Str,soKyTuTai1PhanTuList):
  listTemp=[]
  x=0
  for i in range(0,int(len(Str)/soKyTuTai1PhanTuList)):
    listTemp.append(Str[x:x+soKyTuTai1PhanTuList])
    x=x+soKyTuTai1PhanTuList
  return listTemp
alphabetHoa=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"
    ,"Q","R","S","T","U","V","W","X","Y","Z"]
alphabetThuong=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"
    ,"p","q","r","s","t","u","v","w","x","y","z"]
So=["0","1","2","3","4","5","6","7","8","9"]
kyTuDacBiet=["!","#","$","%","&","'","(",")","*","+",",","-",".","/",":",";"
    ,"<","=",">","?","@","[","\\","]","^","_","`","{","|","}","~","\,","\""]
def checkDangKy(taikhoan,matkhau,nhaplaimatkhau,email,sodienthoai):
    if matkhau!=nhaplaimatkhau:
        return "Mật khẩu nhập lại không khớp"
    elif len(matkhau)<8:
        print(len(matkhau))
        return "Mật khẩu không đủ độ dài tối thiểu 8 ký tự"
    elif thoaManKyTuQuyQuoc(matkhau)==False:
        return "Mật khẩu không đúng dạng quy ước ký tự"
    elif emailCoAcong(email)==False:
        return "Email không đúng dạng quy ước ký tự"
    elif sdtThoaManKyTuQuyUoc(sodienthoai)==False:
        return "Số điện thoại không đúng dạng quy ước ký tự"
    elif thoaManDienDayDuTruong(taikhoan,matkhau,nhaplaimatkhau)==False:
        return "Không được bỏ trống 3 trường nhập đầu"
    elif daTonTai(taikhoan)==True:
        return "Tài khoản đăng ký đã tồn tại"
    return "Bạn đã đăng ký thành công"
def thoaManKyTuQuyQuoc(matkhau):
    coHoa = False
    coThuong = False
    coSo = False
    coKyTuDacBiet = False
    for i in range(0,len(matkhau)):
        if matkhau[i] in alphabetHoa:
            coHoa=True
    for i in range(0, len(matkhau)):
        if matkhau[i] in alphabetThuong:
            coThuong = True
    for i in range(0, len(matkhau)):
        if matkhau[i] in kyTuDacBiet:
            coKyTuDacBiet = True
    for i in range(0, len(matkhau)):
        if matkhau[i] in So:
            coSo = True
    if (coHoa==True) and (coThuong==True) and (coHoa==True) and (coKyTuDacBiet==True) and (coSo==True):
        return True
    return False
def emailCoAcong(email):
    listEmail=string_To_List_PhanTuTrongListLaString(email,1)
    if "@" in listEmail:
        return True
    else:
        return False
def sdtThoaManKyTuQuyUoc(sdt):
    listSDT=string_To_List_PhanTuTrongListLaString(sdt,1)
    print(listSDT)
    for i in listSDT:
        if i not in So:
            return False
    return True


def thoaManDienDayDuTruong(taikhoan,matkhau,nhaplaimatkhau):
    if len(taikhoan)==0 or len(matkhau)==0 or len(nhaplaimatkhau)==0:
        return False
    return True
def sql_DangKy(taikhoan,matkhau,email,sodienthoai,diachi):
    user = User.objects.create_user(taikhoan,email,matkhau)
    user.sodienthoai=sodienthoai
    user.diachi=diachi
    user.save()
def count():
    kma = User.objects.all()
    return len(kma)
def daTonTai(giaTriCheck):
    for i in range(1,count()+1):
        kma = User.objects.get(id=int(i))
        if kma.username==giaTriCheck:
            return True
    return False
def giaTriBamMatMaSHA256(giaTri):
    result = hashlib.sha256(giaTri.encode())
    return result.hexdigest()



