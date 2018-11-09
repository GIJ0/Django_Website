
from django .urls import path
from . import views

app_name="polls"
urlpatterns = [
    path('list/', views.polls_list, name='list'),
    path('details/<int:video_id>/', views.poll_detail, name='detail'),
    path('64/', views.SSB64),
    path('details/<int:video_id>/vote/', views.video_vote, name='vote')

]
