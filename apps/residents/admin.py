from django.contrib import admin
from .models import Resident    
# Register your models here.
@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'house_number', 'is_active')
    search_fields = ('fullname',)