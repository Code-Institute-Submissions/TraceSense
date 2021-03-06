from django.contrib import admin
from .models import Department

# Register your models here.

class Departments(admin.ModelAdmin):
    
    readonly_fields = ('department_id','created','user')
    
    fields = ('department',)
    
    list_display = ('department_id', 'created','department',)
    
admin.site.register(Department,Departments)
