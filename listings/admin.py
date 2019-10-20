from django.contrib import admin

from . models import Listing

# Listings content Admin Class Registration


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_published', 'realtor', 'title', 'city', 'state', 'price',
                    'bedrooms', 'bathrooms', 'garage', 'sqft', 'lot_size')
    list_display_links = ('id', 'realtor', 'title', 'city', 'state',
                          'price', 'bedrooms', 'bathrooms', 'garage', 'sqft', 'lot_size')
    search_fields = ('is_published', 'realtor', 'title', 'city', 'state', 'price',
                     'bedrooms', 'bathrooms', 'garage', 'sqft', 'lot_size')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
