from django.db import models

# Create your models here.
class Meeting(models.Model):
    title = models.CharField(max_length=200, default='Pertemuan RT')
    meeting_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} on {self.meeting_date.strftime('%Y-%m-%d')}"

class MeetingNote(models.Model):
    meeting = models.ForeignKey(
        Meeting, 
        on_delete=models.CASCADE,
        related_name='notes'
        )

    # informasi pertemuan
    place = models.CharField(max_length=200)
    day = models.CharField(max_length=20)
    participant_count = models.PositiveIntegerField()

    # jalanya pertemuan
    mc = models.CharField(
        max_length=50, 
        verbose_name='Pembawa Acara'
        )
    opening_by = models.CharField(
        max_length=50, 
        verbose_name='Pembukaan Acara oleh'
        )
    tahlil_by = models.CharField(
        max_length=50, 
        verbose_name='Tahlil dipimpin oleh'
        )
    prayer_by = models.CharField(
        max_length=50, 
        verbose_name='Doa dipimpin oleh'
        )
    
    # pertemuan berikutnya
    next_meeting = models.CharField(
        max_length=50
        )
    preparation = models.CharField(
        max_length=50
        )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for {self.meeting.title}"

class MeetingCashReport(models.Model):
    note = models.OneToOneField(
        MeetingNote,
        on_delete=models.CASCADE,
        related_name='cash_reports'
        )
    initial_balance = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        default=0
    )
    income = models.DecimalField(
        max_digits=10, 
        decimal_places=0
        )
    expense = models.DecimalField(
        max_digits=10, 
        decimal_places=0
        )
    final_balance = models.DecimalField(
        max_digits=10, 
        decimal_places=0
        )
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Calculate final balance before saving
        self.final_balance = ( 
            self.initial_balance + self.income - self.expense 
            )
        super().save(*args, **kwargs)

class MeetingDiscussion(models.Model):
    note = models.ForeignKey(
        MeetingNote,
        on_delete=models.CASCADE,
        related_name='discussions'
    )
    point = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.point[:50]  # Return the first 50 characters of the discussion point