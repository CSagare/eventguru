from django.contrib import admin
from .models import Eventplanner, contacts

class EventplannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating', 'user_id', 'logo_thumbnail')  # Customize displayed fields

    # Function to display thumbnail of the logo in admin panel
    def logo_thumbnail(self, obj):
        if obj.logo:
            return u'<img src="%s" width="100"/>' % obj.logo.url
        else:
            return '(No logo)'
    logo_thumbnail.allow_tags = True
    logo_thumbnail.short_description = 'Logo'

# Register the Eventplanner model with the admin interface
admin.site.register(Eventplanner, EventplannerAdmin)


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email', 'message')
    list_filter = ('name', 'email')

admin.site.register(contacts, ContactsAdmin)