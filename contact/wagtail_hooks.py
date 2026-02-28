
from wagtail_modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import ContactSubmission

class ContactSubmissionAdmin(ModelAdmin):
    model = ContactSubmission
    menu_label = 'Contact Form'  # ditch this to use verbose_name_plural from model
    menu_icon = 'form'  # change as required
    menu_order = 600  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('name', 'email', 'phone', 'created',)
    # list_filter = ('first_name',)
    search_fields = ('name', 'email', 'phone',)
    
    
modeladmin_register(ContactSubmissionAdmin)