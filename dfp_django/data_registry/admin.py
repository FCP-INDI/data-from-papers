from django.contrib import admin

# Register your models here.
from data_registry.models import Data,Papers,Studies

class DataAdmin(admin.ModelAdmin):
    list_display = ('individual', 'session', 'scan_type','url')
    search_fields = ['individual','session','scan_type']

admin.site.register(Data, DataAdmin)
admin.site.register(Papers)
admin.site.register(Studies)