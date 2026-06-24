from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .forms import (
    MeetingForm,
    MeetingNoteForm,
    MeetingCashReportForm,
    DiscussionFormSet
)

def create_meeting_note(request):
    if request.method == 'POST':
        meeting_form = MeetingForm(request.POST)
        note_form = MeetingNoteForm(request.POST)
        cash_form = MeetingCashReportForm(request.POST)

        if (
            meeting_form.is_valid() 
            and 
            note_form.is_valid() 
            and 
            cash_form.is_valid()
            ):
            meeting = meeting_form.save()
            note = note_form.save(commit=False)
            note.meeting = meeting
            note.save()

            cash_report = cash_form.save(commit=False)
            cash_report.note = note
            cash_report.save()

            discussion_formset = DiscussionFormSet(
                request.POST,
                instance=note
            )

            if discussion_formset.is_valid():
                discussion_formset.save()

            return redirect('meeting_list')
    else:
        meeting_form = MeetingForm()
        note_form = MeetingNoteForm()
        cash_form = MeetingCashReportForm()
        discussion_formset = DiscussionFormSet()

    context = {
        'meeting_form': meeting_form,
        'note_form': note_form,
        'cash_form': cash_form,
        'discussion_formset': discussion_formset,
    }
    return render(request, 'meetings/create_meeting_note.html', context)