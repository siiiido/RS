from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import Query_Table
# Register your models here.
class QueryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40})},
    }
    
    list_display = ('number', 'query','selection1', 'selection2')

admin.site.register(Query_Table, QueryAdmin)