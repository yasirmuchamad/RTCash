from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .forms import (
    MeetingForm,
    MeetingNoteForm,
    MeetingCashReportForm,
    DiscussionFormSet
)
from apps.finance.report import get_cash_report
from .models import Meeting, MeetingNote, MeetingCashReport, MeetingDiscussion

def create_meeting_note(request):
    if request.method == 'POST':
        meeting_form = MeetingForm(request.POST)
        note_form = MeetingNoteForm(request.POST)
        # cash_form = MeetingCashReportForm(request.POST)
        cash_data = get_cash_report()

        if (
            meeting_form.is_valid() 
            and 
            note_form.is_valid() 
            ):
            meeting = meeting_form.save()
            note = note_form.save(commit=False)
            note.meeting = meeting
            note.save()

            # cash_report = cash_form.save(commit=False)
            # cash_report.note = note
            # cash_report.save()

            MeetingCashReport.objects.create(
                note=note,
                initial_balance=cash_data['initial_balance'],
                income=cash_data['income'],
                expense=cash_data['expense'],
                final_balance=cash_data['final_balance']
            )
      
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
        cash_data = get_cash_report()
        discussion_formset = DiscussionFormSet()

    context = {
        'meeting_form': meeting_form,
        'note_form': note_form,
        # 'cash_form': cash_form,`Yass@123
        
        'cash_data': cash_data,
        'discussion_formset': discussion_formset,
    }
    return render(request, 'meetings/create_meeting_notes.html', context)

def meeting_list(request):
    meetings = Meeting.objects.all()
    return render(request, 'meetings/meeting_list.html', {'meetings': meetings})