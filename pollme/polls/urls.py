
from django .urls import path
from . import views

app_name="polls"
urlpatterns = [
    path('list/', views.polls_list, name='list'),
    path('64/', views.SSB64),

]
