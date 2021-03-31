from django.contrib import admin
from TestApp.models import Company
# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display =['Name','ceo','location']
admin.site.register(Company,CompanyAdmin)
