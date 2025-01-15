from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_login(request):
    return redirect('todo:login')  # Update to use namespaced URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_login, name='root'),
    path('todo/', include('todo.urls', namespace='todo')),  # Add namespace
]