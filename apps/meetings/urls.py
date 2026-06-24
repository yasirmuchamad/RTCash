from .views import create_meeting_note

app_name = 'meetings'
urlpatterns = [
    path('create/', create_meeting_note, name='create_meeting_note'),
]