from django.shortcuts import render,redirect
from .forms import AddHomeForm,UpdateBlogForm
from .models import Employee
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='addhome')
def Home(request):
    home = Employee.objects.order_by('-id')[:1]
    context={
        'home':home,
    }
    return render(request,"home.html",context)
def addhome(request):
    home=AddHomeForm()
    if request.method=="POST":
        home=AddHomeForm(request.POST,request.FILES)
        if home.is_valid():
            home.save()
            return redirect('home')
    context={
        'form':home,
    }
    return render(request,'addhome.html',context)

def UpdateBlog(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=="POST":
        edit=UpdateBlogForm(request.POST,instance=employee)
        if edit.is_valid():
            edit.save()
            return redirect('home')
    else:
        edit=UpdateBlogForm(instance=employee)
    context={
        'form':edit,
    }
    return render(request,'updateblog.html',context)