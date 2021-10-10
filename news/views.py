from django.shortcuts import render,get_object_or_404,redirect

from cat.models import Cat
from .models import News
from django.core.files.storage import FileSystemStorage
# Create your views here.
import datetime
from subcat.models import SubCat
from cat.models import Cat
from trending.models import Trending
from myapp.models import article


def detail(request,name):

    article_var = article.objects.get(pk=1)
    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]

    shownews = News.objects.get(name=name)

    popularnews = News.objects.all().order_by('-show')
    popularnews2 = News.objects.all().order_by('-show')[:3]
    tagsname = News.objects.get(name=name).tags
    tags = tagsname.split(',')
    trending = Trending.objects.all().order_by('-pk')[:5]

    try:
        mynews = News.objects.get(name=name)
        mynews.show = mynews.show + 1
        mynews.save()
    except:
        print('cant Add show')


    return render(request,'front/detail.html',{'shownews':shownews,'name':article_var, 'News':news, 'cat':cat,'subcat':subcat,'lastnews':lastnews,'popularnews':popularnews,'popularnews2':popularnews2,"tags":tags,'trending':trending})

def news_list(request):

        # login Check starts HERE
      if not request.user.is_authenticated:
        return redirect('mylogin')
        # login Check Ends HERE


      news = News.objects.all()
      return render(request,'back/news_list.html',{'News':news})

def news_add(request):
    # login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login Check Ends HERE

    now = datetime.datetime.now()
    year  = now.year
    month = now.month
    day = now.day
    if (len(str(day)))==1:
        day = '0' + str(day)
    if (len(str(month)))==1:
        month = '0' + str(month)
    date = (str(year)+'-'+str(month)+'-'+str(day))

    cat = SubCat.objects.all()


    #now = datetime.datetime.now()-datetime.timedelta(days=10)
    #year = now.year
    #month = now.month
    #day = now.day
    #if (len(str(day))) == 1:
     #   day = '0' + str(day)
    #if (len(str(month))) == 1:
     #   month = '0' + str(month)

    #print(str(year) + '/' + str(month) + '/' + str(day))
    #print('xxxxxxxxxxxxx')






    if request.method == "POST":
          news_title = request.POST.get("newstitle")
          cat = request.POST.get("newscat")
          author = request.POST.get("newsauth")
          summary = request.POST.get("newssum")
          body = request.POST.get("newsbody")
          newsid = request.POST.get("newscat")
          tags = request.POST.get("tags")

          if news_title == "" or author == "" or summary == "" or body == "":
              error = "All Fields are required"
              return render(request, 'back/error.html', {'error': error})


          try:
              image = request.FILES['myfiles']
              fs = FileSystemStorage()
              filename = fs.save(image.name, image)
              url = fs.url(filename)




              if str(image.content_type).startswith('image'):

                  if image.size < 5000000:
                      newsname = SubCat.objects.get(pk=newsid).name
                      ocatid = SubCat.objects.get(pk=newsid).catid


                      data = News(name=news_title, author=author,  summary=summary, date=date, picname=filename, picurl=url, catname=newsname, catid=newsid, ocatid=ocatid, show='0',tags=tags)
                      data.save()

                      count = len(News.objects.filter(ocatid=ocatid))

                      data = Cat.objects.get(pk=ocatid)
                      data.count = count
                      data.save()


                      return redirect('news_list')
                  else:
                      error = "Please, You File size is bigger than 5mb"
                      return render(request, 'back/error.html', {'error': error})
              else:
                  fs = FileSystemStorage()
                  fs.delete(str(filename))
                  error = "Please upload valid Image format"
                  return render(request, 'back/error.html', {'error': error})

          except:
              error = " Please upload image "
              return render(request, 'back/error.html', {'error': error})


    return render(request, 'back/news_add.html', {'cat':cat})




def news_delete(request,id):

    # login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login Check Ends HERE

    try:
        b = News.objects.get(pk=id)
        fs = FileSystemStorage()
        fs.delete(str(b.picname))

        ocatid = News.objects.get(pk=id).ocatid

        b.delete()

        count = len(News.objects.filter(ocatid=ocatid))
        m = Cat.objects.get(pk=ocatid)
        m.count = count
        m.save()




    except:
        error = "something went wrong"
        return render(request, 'back/error.html', {'error': error})
    return redirect('news_list')


def news_edit(request, id):

    # login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login Check Ends HERE

    if len(News.objects.filter(pk=id)) ==0:

        error = "This News Does not Exist"
        return render(request, 'back/error.html', {'error': error})

    news = News.objects.get(pk=id)
    cat = SubCat.objects.all()

    if request.method == "POST":
        news_title = request.POST.get("newstitle")
        cat = request.POST.get("newscat")
        summary = request.POST.get("newssum")
        body = request.POST.get("newsbody")
        newsid = request.POST.get("newscat")
        tags = request.POST.get("tags")

        if news_title == "" or summary == "" or body == "":
            error = "All Fields are required"
            return render(request, 'back/error.html', {'error': error})

        try:
            image = request.FILES['myfiles']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            url = fs.url(filename)

            if str(image.content_type).startswith('image'):

                if image.size < 5000000:
                    newsname = SubCat.objects.get(pk=newsid).name

                    b = News.objects.get(pk=id)

                    fss = FileSystemStorage()
                    fss.delete(str(b.picname))

                    b.name = news_title
                    b.summary=summary
                    b.picname=filename
                    b.picurl=url
                    b.catname=newsname
                    b.catid=newsid
                    b.tags = tags
                    b.save()

                    return redirect('news_list')
                else:
                    error = "Please, You File size is bigger than 5mb"
                    return render(request, 'back/error.html', {'error': error})
            else:
                fs = FileSystemStorage()
                fs.delete(str(filename))
                error = "Please upload valid Image format"
                return render(request, 'back/error.html', {'error': error})




        except:

            newsname = SubCat.objects.get(pk=newsid).name
            b = News.objects.get(pk=id)

            b.name = news_title
            b.summary = summary
            b.catname = newsname
            b.catid = newsid
            b.tags = tags
            b.save()

    return render(request,'back/news_edit.html',{'id':id, 'news':news, 'cat':cat})