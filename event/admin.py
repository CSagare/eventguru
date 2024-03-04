from django.contrib import admin
from .models import Eventplanner, contacts
from .models import category, planner_category

class EventplannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating', 'user_id', 'logo')  # Customize displayed fields

    # Function to display thumbnail of the logo in admin panel
    # def logo_thumbnail(self, obj):
    #     if obj.logo:
    #         # return u'<img src="%s" width="100"/>' % obj.logo.url
    #         #   return '<img src="{}" width="100">'.format(obj.logo.url)

    #         return u'<%s>' % obj.logo.url
    #     else:
    #         return '(No logo)'
    # logo_thumbnail.allow_tags = True
    # logo_thumbnail.short_description = 'Logo'

    



# Register the Eventplanner model with the admin interface
admin.site.register(Eventplanner, EventplannerAdmin)


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email', 'message')
    list_filter = ('name', 'email')

admin.site.register(contacts, ContactsAdmin)
# admin.site.register(Event)


@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(planner_category)
class PlannerCategoryAdmin(admin.ModelAdmin):
    list_display = ('eventplanner', 'category')

