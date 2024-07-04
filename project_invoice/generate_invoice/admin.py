from django.contrib import admin


from generate_invoice.models import Contact, Products


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country')  # Fields to display in the list view
    search_fields = ('name', 'city')  # Fields to include in the search functionality


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('nazwa','index', 'kodcelny', 'cena')
    search_fields = ('index', 'kodcelny')


admin.site.site_header = 'Invoicy'
admin.site.register(Contact, ContactAdmin)
admin.site.register(Products, ProductsAdmin)
# Re-register UserAdmin
