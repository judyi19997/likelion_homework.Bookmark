from django.contrib import admin
from .models import bookmarkModel

# Register your models here.
class bookmarkadmin(admin.ModelAdmin):
    list_display = ['id', 'site_name', 'site_url']

admin.site.register(bookmarkModel,bookmarkadmin)
