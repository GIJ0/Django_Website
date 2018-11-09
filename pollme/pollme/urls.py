
from django.contrib import admin

from django.contrib import admin
from django.urls import path
from . import views
from django .contrib import admin
from django .urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('submit/', views.submit),
    path('polls/', include('polls.urls', namespace='polls')),
    path('N64/', views.N64),

]

