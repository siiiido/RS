from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import Matching_Table

# Register your models here.

class ResultAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
    }
    
    list_display = ('user_man_id', 'user_woman_id')
    

admin.site.register(Matching_Table, ResultAdmin)