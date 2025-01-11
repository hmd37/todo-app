from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('tasks.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
