from django.urls import path
from .views import create_meeting_note, meeting_list

app_name = 'meetings'
urlpatterns = [
    path('create/', create_meeting_note, name='create_meeting_note'),
    path('list/', meeting_list, name='meeting_list'),
]