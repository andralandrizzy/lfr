from django.contrib import admin
from . models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('name', 'listing', 'email')
    list_filter = ('name',)
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
