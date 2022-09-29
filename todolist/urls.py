from django.urls import path
from .views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='list_task'),
    path('create_task/',create_task , name='create_task'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]