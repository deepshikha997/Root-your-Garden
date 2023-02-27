from audioop import add
from email.mime import image
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .models import *
# Create your views here.
def register(request):
    if request.method=="POST":
        fn=request.POST['fname']
        ln=request.POST['lname']
        un=request.POST['uname']
        em=request.POST['email']
        paw=request.POST['pwd']
        cpaw=request.POST['cpas']
        if paw==cpaw:
            usr=User.objects.create_user(username=un,first_name=fn,last_name=ln,email=em,password=paw)
            usr.save()
            pf=profile(usr=usr)
            pf.save()
            return redirect("lgt")
        else:
            messages.info(request,"Password not matching")
            return redirect("register")
    return render(request,"register.html")
def gardenreg(request):
    if request.method=="POST":
        fn=request.POST['fname']
        ln=request.POST['lname']
        un=request.POST['uname']
        em=request.POST['email']
        paw=request.POST['pwd']
        cpaw=request.POST['cpas']
        if paw==cpaw:
            usr=User.objects.create_user(username=un,first_name=fn,last_name=ln,email=em,password=paw)
            if "accept" in request.POST:
                usr.is_staff=True
            usr.save()
            return redirect("lgt")
        else:
            messages.info(request,"Password not matching")
            return redirect("register")
    return render(request,"gardenreg.html")


    
def login(request):
    if (request.method=="POST"):
        un=request.POST['uname']
        paw=request.POST['pwd']
        lg=auth.authenticate(request,username=un,password=paw)
        print(un,paw)
        print(lg)
        if lg != None:
            if lg.is_staff==True:
               auth.login(request,lg)
               return redirect("index2")
            else:
                auth.login(request,lg)
            
                auth.login(request,lg)
                return redirect('index')
        else:
              messages.info(request,"invalid credentials")
              return redirect('lgt')       
    else:
        return render(request,"login.html")
# def login(request):
#     if(request.method=="POST"):
#         uname=request.POST['uname']
#         pas=request.POST['pwd']
#         user=auth.authenticate(username=uname,password=pas)
#         print(uname,pas,user)
#         if user != None:
#             if user.is_staff==True:
#                 auth.login(request,user)
#                 return redirect("repaj")
#             else:
#                 auth.login(request,user)
            
#                 auth.login(request,user)
            
#             return redirect('home')
#         else:
#               messages.info(request,"invalid credentials")
#               return redirect('lgt')       
#     else:
#         return render(request,"login.html")
    
def logout(request):
    auth.logout(request)
    return redirect("index")
def Prof(request):
    dis={}
    pro=profile.objects.filter(usr__id=request.user.id)
    if len(pro)>0 :
        prf=profile.objects.get(usr__id=request.user.id)
        dis['prd']=prf
    return render(request,"profile.html",dis)

def uppro(request):
    display={}
    prof=profile.objects.filter(usr_id=request.user.id)
    if len(prof)>0:
        dis=profile.objects.get(usr_id=request.user.id)
        display["data"]=dis
        if request.method=="POST":
            fname=request.POST["fname"]
            lname=request.POST["lname"]
            email=request.POST['email']
            ph_pro=request.POST['phone']
            addr_pro=request.POST['add']
         
            up_user=User.objects.get(id=request.user.id)
            up_user.first_name=fname
            up_user.last_name=lname
            up_user.email=email
            up_user.save()
            dis.ph_pro=ph_pro
            dis.addr_pro=addr_pro
            dis.save()
            if "imgs" in request.FILES:
                img=request.FILES["imgs"]
                dis.img_pro=img
                dis.save()
                messages.info(request,"Image uploaded successfully")
                return redirect("uppro")
            messages.info(request,"profile uploaded successfully")
            return redirect("uppro")
    return render(request,"uppro.html",display)

def recoverpwd(request):
    if (request.method=="POST"):
        current=request.POST["cpwd"]       
        paw=request.POST['npwd']
        user=User.objects.get(id=request.user.id)
        un=user.username
        paw=paw
        check=user.check_password(current)
        if check==True:
                user.set_password(paw)
                user.save()
                auth.authenticate(request,username=un,password=paw)
                messages.info(request," Password Changed Successfully !!!")
                return redirect("lgt")
        else:
                 messages.info(request,"Incorrect Current Password")
                 return redirect("recover") 
    #         usr=User.objects.create_user(password=paw)
    #         usr.save()
    #         pf=profile(usr=usr)
    #         pf.save()
    #         return redirect("recover")
    #     else:
    #         messages.info(request,"Password not matching")
    #         return redirect("recover")
    return render(request,'recover-password.html')
def Pwdcomplete(request):
    return render(request,'password_reset_complete.html')

    
