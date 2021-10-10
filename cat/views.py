from django.shortcuts import render,get_object_or_404,redirect
from .models import Cat


# Create your views here.
def cat_list(request):
    # login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login Check Ends HERE

    cat = Cat.objects.all()

    return render(request, 'back/cat_list.html', {'cat':cat})

def cat_add(request):

    # login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login Check Ends HERE

    if request.method == "POST":
        name = request.POST.get('name')
        if name == "":
            error = "All Fields are required"
            return render(request, 'back/error.html', {'error': error})

        if len(Cat.objects.filter(name=name))  !=0:
            error = "category Exist"
            return render(request, 'back/error.html', {'error': error})

        b = Cat(name=name)
        b.save()
        return redirect('cat_list')

    return render(request, 'back/cat_add.html')


def cat_del(request,id):
    # login Check starts HERE
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login Check Ends HERE

    b = Cat.objects.filter(pk=id)
    b.delete()

    return redirect('cat_list')
