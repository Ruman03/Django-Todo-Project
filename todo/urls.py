from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'todo'  # Add namespace

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='todo/logout.html',
    ), name='logout'),
    path('register/', views.register, name='register'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
]
