from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
import datetime
import news
from .models import article
from news.models import News
from cat.models import Cat
from trending.models import Trending
from subcat.models import SubCat
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from manager.models import Manager


def index(request):


   article_var = article.objects.get(pk=1)
   news = News.objects.all().order_by('-pk')
   cat = Cat.objects.all()
   subcat = SubCat.objects.all()
   lastnews = News.objects.all().order_by('-pk')[:3]

   popularnews = News.objects.all().order_by('-show')
   popularnews2 = News.objects.all().order_by('-show')[:3]
   trending = Trending.objects.all().order_by('-pk')[:5]

   return render(request, 'front/index.html',{'name':article_var, 'News':news, 'cat':cat,'subcat':subcat,'lastnews':lastnews, 'popularnews2':popularnews2,'trending':trending})

def about(request):
    article_var  = article.objects.get(pk=1)

    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]

    popularnews = News.objects.all().order_by('-show')
    popularnews2 = News.objects.all().order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]

    return render(request, 'front/about.html',{'name':article_var, 'News':news, 'cat':cat,'subcat':subcat,'lastnews':lastnews, 'popularnews2':popularnews2,'trending':trending})


def admin_panel(request):
    # login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login Check Ends HERE
    return render(request,'back/home.html')


def mylogin(request):

    if request.method == 'POST':
        user = request.POST.get('username')
        upass = request.POST.get('password')

        if user !="" and upass!="":
           user = authenticate(username=user,password=upass)

           if user != None:
               login(request,user)
               return redirect('panel')

        print(user,upass)
    return render(request, 'front/login.html')



def myregister(request):


    if request.method == 'POST':

        name = request.POST.get('name')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if name ==  "" :
            msg = 'Name field Is required'
            return render(request,'front/message.html', {'msg':msg})

        if password != password1 :
            msg = 'Password is wrong'
            return render(request, 'front/message.html', {'msg':msg})

        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0

        for i in password:
            if i > '0' and i < '9':
                count1 += 1
            if i > 'A' and i < 'Z':
                count2 += 1
            if i > 'a' and i < 'z':
                count3 += 1
            if i > '!' and i < ')':
                count4 += 1
        count = count1 + count2 + count3 + count4
        strength = len(password)
        if count >= 1 and strength < 8:
            msg = 'Weak password'
            return render(request, 'front/message.html', {'msg': msg})

        if len(User.objects.filter(username=uname))== 0 and len(User.objects.filter(email=email))== 0:
            user = User.objects.create_user(username=uname, email=email, password=password)

            b = Manager(name=name,uname=uname,email=email)
            b.save()

    return render(request, 'front/login.html')


def mylogout(request):

    logout(request)

    return redirect('mylogin')

def site_settings(request):

    # login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login Check Ends HERE
    prem = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': prem = 1

    if prem == 0:
        error = 'Access Denied'
        return render(request, 'back/error.html', {'error': error})

    if request.method == 'POST':

        title = request.POST.get('title')
        body = request.POST.get('body')
        fb = request.POST.get('fb')
        tw = request.POST.get('tw')
        yt = request.POST.get('yt')
        ph = request.POST.get('ph')

        if fb == "": fb = '#'
        if tw == "": tw = '#'
        if yt == "": yt = '#'


        if title == "" or body == "" or ph == "":
            error = 'All Field are required'
            return render(request, 'back/error.html', {'error':error})



        try:

            b = article.objects.get(pk=1)
            image = request.FILES['myfiles']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            url = fs.url(filename)

            picurl = url
            picname = filename

        except:

            picurl = "_"
            picname = "_"

        try:

            b = article.objects.get(pk=1)
            image2 = request.FILES['myfiles2']
            fs2 = FileSystemStorage()
            filename2 = fs2.save(image2.name, image2)
            url2 = fs.url(filename2)

            picurl2 = url2
            picname2 = filename2

        except:

            picurl2 = "_"
            picname2 = "_"

        b.title = title
        b.body = body
        b.fb = fb
        b.tw = tw
        b.yt = yt
        b.ph = ph
        b.picurl = picurl
        b.picname = picname
        b.picurl2 = picurl2
        b.picname2 = picname2
        b.save()

    site = article.objects.get(pk=1)
    return render(request, 'back/settings.html', {'site':site})

def about_settings(request):
    # login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login Check Ends HERE
    prem = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': prem = 1

    if prem == 0:
        error = 'Access Denied'
        return render(request, 'back/error.html', {'error': error})

    if request.method == 'POST':
        body = request.POST.get('aboutbody')
        if body == '':
            error = 'All Field are required'
            return render(request, 'back/error.html', {'error': error})
        v = article.objects.get(pk=1)
        v.bodylong = body
        v.save()


    aboutbody = article.objects.get(pk=1).bodylong



    return render(request, 'back/about_setting.html', {'aboutbody':aboutbody} )



def contact(request):
    article_var  = article.objects.get(pk=1)

    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]

    popularnews = News.objects.all().order_by('-show')
    popularnews2 = News.objects.all().order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]


    return render(request, 'front/contact.html',{'name':article_var, 'News':news, 'cat':cat,'subcat':subcat,'lastnews':lastnews, 'popularnews2':popularnews2,'trending':trending})




def change_pass(request):

    # login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login Check Ends HERE

    if request.method == 'POST':

        oldpass = request.POST.get('oldpass')
        newpass = request.POST.get('newpass')

        if oldpass =="" or newpass =="":
            error = 'Your Password is Incorrect'
            return render(request, 'back/error.html', {'error': error})

        user = authenticate(username=request.user, password=oldpass)


        if user != None:


            if len(newpass) < 8 :
                error = 'Your Password is needs to be atleast 8 characters'
                return render(request, 'back/error.html', {'error': error})

            count1 = 0
            count2 = 0
            count3 = 0
            count4 = 0

            for i in newpass:
                if i > '0' and i < '9':
                    count1 += 1
                if i > 'A' and i < 'Z':
                    count2 += 1
                if i > 'a' and i < 'z':
                    count3 += 1
                if i > '!' and i < ')':
                    count4 += 1
            count =  count1 + count2 + count3 + count4
            if count >= 1:
                user = User.objects.get(username=request.user)
                user.set_password(newpass)
                user.save()
                return redirect('mylogout')




        else:
            error = 'All Field are required'
            return render(request, 'back/error.html', {'error': error})

    return render(request, 'back/changepass.html')