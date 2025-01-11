from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


def redirect_to_lists(request):
    return redirect('/todo/lists/')

urlpatterns = [
    path('', redirect_to_lists),
    path('admin/', admin.site.urls),
    path('todo/', include('tasks.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
