from django.contrib import admin

from . models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_mvp', 'name', 'phone',
                    'email', 'description', 'hire_date')
    list_display_links = ('id', 'name', 'phone',
                          'email', 'description', 'hire_date')
    search_fields = ('is_mvp', 'name', 'phone', 'email',
                     'description', 'hire_date')
    list_filter = ('name',)
    list_editable = ('is_mvp',)
    list_per_page = 25


admin.site.register(Realtor, RealtorAdmin)
