from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import Registered_User_Table
class MainAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
    }
    
    list_display = ('user_id', 'user_nickname', 'sign_up_date', 'university', 'image_tag', 'admin_allow')
    list_display_links = ['user_id', 'image_tag']
    list_editable = ['admin_allow']

    list_filter = ('gender', 'admin_allow', 'university', 'age_range')

admin.site.register(Registered_User_Table, MainAdmin)