import csv

from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea


from .models import *

# Register your models here.
class AllAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
    }

admin.site.register(Social_User_Table, AllAdmin)

# class AllowAdmin(admin.ModelAdmin):
#     list_display = ('user_id', 'university', 'sign_up_date', 'image', 'admin_allow')

    

# admin.site.register(Social_User_Table, AllowAdmin)