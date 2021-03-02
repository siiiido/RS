from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import Registered_User_Table
class MainAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
    }
    
    list_display = ('user_id', 'user_nickname', 'gender', 'university', 'contact', 'last_partner_user_id',
                 'sign_up_date', 'last_update_date', 'recent_matching_date', 'matching_count')
    list_filter = ('gender', 'university', 'matching_count')

admin.site.register(Registered_User_Table, MainAdmin)