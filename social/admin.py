from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import Social_User_Table

# Register your models here.
# class AllAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
#     }
    
#     list_display = ('user_id', 'sign_up_date', 'university', 'image_tag', 'admin_allow')

# admin.site.register(Social_User_Table, AllAdmin)

class UserAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
    }
    
    list_display = ('user_id', 'sign_up_date', 'university', 'image_tag', 'admin_allow')
    list_filter = ('gender', 'admin_allow', 'university', 'age_range')


admin.site.register(Social_User_Table, UserAdmin)

