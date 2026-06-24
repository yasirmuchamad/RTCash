from django import forms
from .models import Meeting, MeetingNote, MeetingCashReport, MeetingDiscussion  
from django.forms import inlineformset_factory
    
class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['title', 'meeting_date']
        widgets = {
            'meeting_date': forms.DateInput(attrs={'type': 'date'}),
        }

class MeetingNoteForm(forms.ModelForm):
    class Meta:
        model = MeetingNote
        exclude = ['meeting']

class MeetingCashReportForm(forms.ModelForm):
    class Meta:
        model = MeetingCashReport
        exclude = ['note', 'final_balance']

class MeetingDiscussionForm(forms.ModelForm):
    class Meta:
        model = MeetingDiscussion
        exclude = ['note']

DiscussionFormSet = inlineformset_factory(
    MeetingNote, 
    MeetingDiscussion, 
    form=MeetingDiscussionForm, 
    extra=3, 
    can_delete=True
)
