from django.contrib import admin

# Register your models here.
from .models import (
    Meeting, 
    MeetingNote, 
    MeetingCashReport, 
    MeetingDiscussion
    )

admin.site.register(Meeting)
admin.site.register(MeetingNote)
admin.site.register(MeetingCashReport)
admin.site.register(MeetingDiscussion)