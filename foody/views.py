from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import *
import random


changes=[]
changed={}


def home(request):
    return render(request,"homes.html")


def veg(request,*kwargs,**args):
    obj=Veg.objects.all()
    if request.method=="POST":
        """ld=request.POST.get('order_id')
        orders=Veg_order.objects.get(id=int(ld))
        orders(name="madhu")"""
        for i in obj:
            c=int(i.cost)
            q=0
            try:
                q=int(request.POST.get(str(i.id)))
            except:
                pass;
            cal=c*q
            print(cal)
            Veg_order(name=i.name,img=i.img,cost=c,quantity=q,total=cal).save()
            """ c=Veg.objects.all().count()
            obj1=Veg_order.objects.all()[Veg_order.objects.all().count()-c:]
        return render(request,"veg.html",{'objs':obj1})"""
        return redirect("/non_veg")
    return render(request,"veg.html",{'objs':obj})

def non_veg(request):
    obj=Non_veg.objects.all()
    if request.method=="POST":
        """ld=request.POST.get('order_id')
        orders=Veg_order.objects.get(id=int(ld))
        orders(name="madhu")"""
        for i in obj:
            c=int(i.cost)
            q=0
            try:
                q=int(request.POST.get(str(i.id)))
            except:
                pass;
            cal=c*q
            print(cal)
            Non_veg_order(name=i.name,img=i.img,cost=c,quantity=q,total=cal).save()
        return redirect("/snacks")
    return render(request,"non_veg.html",{"objs":obj})

def register(request):
    if request.method=="POST":
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        username=request.POST['username']
        emailid=request.POST['emailid']
        password1=request.POST['password1']
        password2=request.POST['password2']
        address=request.POST['address']
        li=[first_name,last_name,username,emailid,password1,password2,address]
        if "" in li:
            messages.info(request,"please fill all the fields")
        elif len(password1)<8:
            messages.info(request,'length of password must be greater than 8')
        elif password1==password2:
            if not Users.objects.filter(username=username).exists():
                if not Users.objects.filter(emailid=emailid).exists():
                    if not Users.objects.filter(password=password1).exists():
                        obj=Users(first_name=first_name,last_name=last_name,username=username,emailid=emailid,password=password1,address=address)
                        obj.save()

                        subject="foody registration status"
                        message="Dear "+first_name+" "+last_name+"\n"+"\t Your account has been registered successfully.\t Now you are a foody customer."
                        if send_mail(subject,message,settings.EMAIL_HOST_USER,[emailid],fail_silently=False):
                            return redirect("/")
                        else:
                            messages.info(request,"email is not valid")

                        return redirect("/")
                    else:
                        messages.info(request,"someone has already used this password")
                else:
                    messages.info(request,"emailid already exists")
            else:
                messages.info(request,"username already exists")
        else:
            messages.info(request,"passwords are not matching")
        return render(request,"register.html",{"first_name":first_name,"last_name":last_name,"username":username,"emailid":emailid,"address":address})

    else:
        return render(request,"register.html")


def bill(request):
    rows=Veg.objects.all().count()
    orders_veg=Veg_order.objects.all()
    grand=0
    for i in orders_veg:
        grand+=int(i.total)
    orders_non_veg=Non_veg_order.objects.all()
    for i in orders_non_veg:
        grand+=int(i.total)
    orders_snacks=Snacks_order.objects.all()
    for i in orders_snacks:
        grand+=int(i.total)
    orders_soft_drinks=Soft_drinks_order.objects.all()
    for i in orders_soft_drinks:
        grand+=int(i.total)
    messages.info(request,"Your grand total is "+str(grand)+"$ only")
    return render(request,"bill.html",{"orders_veg":orders_veg,"orders_non_veg":orders_non_veg,"orders_snacks":orders_snacks,"orders_soft_drinks":orders_soft_drinks})



def forget_pass(request):
    if request.method=='POST':
        new=request.POST['otp']
        print(len(changes))
        username=changes[len(changes)-1]
        print(changed[username])
        if int(new)==changed[username]:
            return render(request,"reset.html")
        else:
            messages.info(request,"WRONG OTP")
    else:
        num=random.randint(100000,999999)
        print(len(changes))
        username=changes[len(changes)-1]
        changed[username]=num
        print(changed)
        y=Users.objects.get(username=username)
        if y is not None:
            emailid=y.emailid
            print(emailid)
            subject="Foody OTP status"
            message="Your One Time Password (OTP)  is:"+str(num)
            if not send_mail(subject,message,settings.EMAIL_HOST_USER,[y.emailid],fail_silently=False):
                messages.info(request,"email is not valid")
        else:
            messages.info(request,"this is user in not a member of Foody")
            return redirect("login")
    return render(request,"forget_pass.html")


def snacks(request):
    obj=Snacks.objects.all()
    if request.method=="POST":
        for i in obj:
            c=int(i.cost)
            q=0
            try:
                q=int(request.POST.get(str(i.id)))
            except:
                pass;
            cal=c*q
            print(cal)
            Snacks_order(name=i.name,img=i.img,cost=c,quantity=q,total=cal).save()
        return redirect("/soft_drinks")
    return render(request,"snacks.html",{"objs":obj})


def soft_drinks(request):
    obj=Soft_drinks.objects.all()
    if request.method=="POST":
        for i in obj:
            c=int(i.cost)
            q=0
            try:
                q=int(request.POST.get(str(i.id)))
            except:
                pass;
            cal=c*q
            print(cal)
            Soft_drinks_order(name=i.name,img=i.img,cost=c,quantity=q,total=cal).save()
        return redirect("/bill")
    return render(request,"soft_drinks.html",{"objs":obj})



def thanq(request):
    Veg_order.objects.all().delete()
    Non_veg_order.objects.all().delete()
    Snacks_order.objects.all().delete()
    Soft_drinks_order.objects.all().delete()
    return render(request,"thanq.html")

def super_admin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        if len(password)>8:
            s=captains(username=username,password=password)
            s.save()
            messages.info(request,username+" is an admin now")
        else:
            messages.info(request,"password length must be greater than 8")
    return render(request,"super_admin.html")

def login_super_admin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        print(username)
        if username=="imran" and password=="987654321":
            return render(request,"super_admin.html")
        else:
            messages.info(request,"invalid details")
    return render(request,"login_super_admin.html")

def admin1(request):
    return render(request,"admin1.html")

def add_item(request):
    if request.method=="POST":
        category=request.POST['category'].lower()
        name=request.POST['name']
        img=request.POST['doc']
        s=None
        cost=int(request.POST['cost'])
        try:
            if category=="veg":
                s=Veg(name=name,img=img,cost=cost)
            elif category=="non-veg" or category=="non_veg":
                s=Non_veg(name=name,img=img,cost=cost)
            elif category=="snacks":
                s=Snacks(name=name,img=img,cost=cost)
            elif category=="soft-drinks" or category=="soft_drinks":
                s=Soft_drinks(name=name,img=img,cost=cost)
            else:
                messages.info(request,"invalid category")
            if not s.save():
                messages.info(request,"item saved successfullly")
            else:
                messages.info(request,"item not saved")
        except:
            messages.info(request,"fill all the fields without invalid data")
        return render(request,"add_item.html")
    else:
        return render(request,"add_item.html")


def change(request):
    if request.method=='POST':
        category=request.POST['category']
        name=request.POST['name']
        cost=request.POST['cost']
        li=[name,cost]
        if "" in li:
            messages.info(request,"please fill all the fields")
        elif category=='veg':
            if Veg.objects.filter(name=name).exists():
                x=Veg.objects.get(name=name)
                x.cost=cost
                x.save()
                messages.info(request,"Cost of "+name+" has changed successfully in "+category+" category")
            else:
                messages.info(request,name+" doesnot exist in "+category)
        elif category=="non-veg" or category=="non_veg":
            if Non_veg.objects.filter(name=name).exists():
               x= Non_veg.objects.get(name=name)
               x.cost=cost
               x.save()
               messages.info(request,"Cost of "+name+" has changed successfully in "+category+" category")
            else:
                messages.info(request,name+" doesnot exist in "+category)
        elif category=="snacks":
            if Snacks.objects.filter(name=name).exists():
               x=Snacks.objects.get(name=name)
               x.cost=cost
               x.save()
               messages.info(request,"Cost of "+name+" has changed successfully in "+category+" category")
            else:
                messages.info(request,name+" doesnot exist in "+category)
        elif category=="soft-drinks" or category=="soft_drinks":
            if Soft_drinks.objects.filter(name=name).exists():
               x=Soft_drinks.objects.get(name=name)
               x.cost=cost
               x.save()
               messages.info(request,"Cost of "+name+" has changed successfully in "+category+" category")
            else:
                messages.info(request,name+" doesnot exist in "+category)
        else:
            messages.info(request,"invalid category")
    return render(request,"change.html")


def login_admin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        if captains.objects.filter(username=username,password=password):
            return render(request,"admin1.html")
        else:
            messages.info(request,"invalid details")
    return render(request,"login_admin.html")


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        changes.append(username)
        print(changes)
        if Users.objects.filter(username=username,password=password):
            #veg(request)
            obj=Veg.objects.all()
            return redirect('/veg')
        else:
            messages.info(request,"username or password is wrong")
    return render(request,"homes.html")


def reset(request):
    if request.method=='POST':
        password1=request.POST['password1']
        password2=request.POST['password2']
        if len(password1)<8:
            messages.info(request,"length of password must be greater than 8")
        if password1==password2:
            if Users.objects.filter(password=password1).exists():
                messages.info(request,"password already exist try another")
            else:
                x=Users.objects.get(username=changes[len(changes)-1])
                x.password=password1
                x.save()
                subject="Password status"
                message="password has been changed successfully"
                if not send_mail(subject,message,settings.EMAIL_HOST_USER,[x.emailid],fail_silently=False):
                    messages.info(request,"email is not valid")
                else:
                    return redirect("/")
        else:
            messages.info(request,'passwords are not matching')
    return render(request,"reset.html")


def delete_item(request):
    if request.method=='POST':
        category=request.POST['category'].lower()
        name=request.POST['name']
        li=[category,name]
        if "" in li:
            messages.info(request,"please fill all the fields")
        elif category=='veg':
            if Veg.objects.filter(name=name).exists():
                Veg.objects.filter(name=name).delete()
                messages.info(request,name+" is deleted successfully in "+category+" category")
            else:
                messages.info(request,name+" doesnot exist in "+category)
        elif category=="non-veg" or category=="non_veg":
            if Non_veg.objects.filter(name=name).exists():
                Non_veg.objects.filter(name=name).delete()
                messages.info(request,name+" is deleted successfully in "+category+" category")
            else:
                messages.info(request,name+" doesnot exist in "+category)
        elif category=="snacks":
            if Snacks.objects.filter(name=name).exists():
               Snacks.objects.filter(name=name).delete()
               messages.info(request,name+" is deleted successfully in "+category+" category")
            else:
                messages.info(request,name+" doesnot exist in "+category)
        elif category=="soft-drinks" or category=="soft_drinks":
            if Soft_drinks.objects.filter(name=name).exists():
               Soft_drinks.objects.filter(name=name).delete()
               messages.info(request,name+" is deleted successfully in "+category+" category")
            else:
                messages.info(request,name+" doesnot exist in "+category)
        else:
            messages.info(request,"invalid category")
       
    return render(request,"delete_item.html")

def change_order(request):
    Veg_order.objects.all().delete()
    Non_veg_order.objects.all().delete()
    Snacks_order.objects.all().delete()
    Soft_drinks_order.objects.all().delete()
    return redirect("/veg")

def cancel(request):
    Veg_order.objects.all().delete()
    Non_veg_order.objects.all().delete()
    Snacks_order.objects.all().delete()
    Soft_drinks_order.objects.all().delete()
    return redirect("/")