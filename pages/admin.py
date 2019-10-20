from django.contrib import admin
from . models import Client
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_link', 'date_added')
    list_display_links = ('id', 'client_link', 'date_added')
    list_filter = ('client_link',)
    search_fields = ('client_link',)
    list_per_page = 25


admin.site.register(Client, ClientAdmin)
