from django.shortcuts import render
from todolist.models import Task
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.form import TaskForm

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_task = Task.objects.filter(user = request.user)
    context = {
    'list_task': data_task,
    'currently_user' : request.user,
    "nama" : "Inez Bungaria Octaviana Pardede",
    "npm" : "2106751833"
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:create_task")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response
# Create your views here.

def create_task(request):
    form_todolist=TaskForm()
    #instance = Task.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form_todolist = TaskForm(request.POST or None, request.FILES or None)
        print(form_todolist)
        if form_todolist.is_valid():
            task=form_todolist.save(commit=False)
            task.user=request.user
            task.save()
            print(request.user)
            #form_todolist.save()
            messages.success(request, (f"Task berhasil dibuat"))
            return redirect('todolist:list_task')
        else:
             print("Form tidak valid")

    context = {
        'form_todolist' : form_todolist,
        'title' : "Tambah Task",     
        }
    return render(request, "create_todolist.html", context)

def task_status(request, update_task):
    data_update = Task.objects.get(id=update_task)

    if data_update.is_finished:
        data_update.is_finished = False
    else:
        data_update.is_finished = True

    data_update.save() 
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

def delete_task(request, update_task):
    data_update = Task.objects.get(id=update_task)
    if data_update == request.user:
        data_update.delete()
    return redirect('todolist:show_todolist')
