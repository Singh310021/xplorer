from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth
from ad_app.forms import guide_form
from django.contrib import messages
# Create your views here.
def home (request):
   activity = Activity.objects.all()
   data = Adventure.objects.all()
   return render(request,"home.html",{"activity":activity,"data":data})


def filteractivity(request,id):
   activity = Activity.objects.all()
   activityfilter = Activity.objects.get(id=id)
   data = Adventure.objects.filter(activity=activityfilter)
   return render(request,"home.html",{"data":data,"activity":activity})

def ReadMore(request,id):
    data = Adventure.objects.get(id=id)
    print(data.place)
    guide = Guide.objects.filter(Guide_location=data.place)  
    offer = Offers.objects.filter(place=data.id)
    return render(request,"readmore.html",{"data":data,"guide":guide,'offer':offer})



def login(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user:
            auth.login(request,user)
            return redirect("about")
        else:
            return redirect("login")

    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("login")

def signup(request):
    if request.method =="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        User.objects.create_user(username=username,email=email,password=password)
        return redirect("login")


    return render(request,"signup.html")


def guide_function(request):
    try:
         data = Guide.objects.filter(Username=request.user)
         if data:
             return redirect("guidedata")
         else:
            if request.method  == "GET":
                form = guide_form()
                return render(request,"guidelogin.html",{'form':form})
            else:
                form = guide_form(request.POST,request.FILES)
                if form.is_valid():
                    form.save()
                    
            return render(request,"guidelogin.html")
    except Exception as e:
        print(e)
        return render(request,"guidelogin.html")

from .models import Guide

def guidedata(request):
    try:    
        data = Guide.objects.filter(Username=request.user)
        return render(request,"guidedata.html",{'data':data})
    except Exception as e:
        print(e)
    return render(request,"guidedata.html")


def about(request):
    return render(request,"newabout.html")

def help(request):
   if request.method == "POST":
        name = request.POST['username']
        email = request.POST['email']
        problem = request.POST['problem']
        data = Help.objects.create(username=name,email=email,problem=problem)
        if data:
            context = {
                "msg":f'Thanks {request.user} For Your Response'
            }
        return render(request,"help.html",context)
   else:
    return render(request,"help.html")


def search(request):
    if request.method == 'POST':
        srcinp = request.POST['srcinp']
        if Place.objects.filter(place__contains=srcinp).exists():
            plcid = Place.objects.get(place__contains=srcinp)
            data = Adventure.objects.filter(place=plcid)
            return render(request,'search.html',{'data':data})
        else:
            messages.error(request,'NO SEARCH RESULT')
            return redirect('home')
    else:
          return redirect('home')

def footer(request):
    return render(request,"footer.html")  
