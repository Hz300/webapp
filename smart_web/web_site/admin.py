from django.contrib import admin
from django.contrib.admin import TabularInline
from .models import SMRTPROPERTIES, PropertyImage, SMRTWEBFORM, Asociados

# Define an inline form for managing PropertyImage objects
class PropertyImageInline(TabularInline):
    model = PropertyImage
    extra = 1  # Allow adding 1 image initially

# Register the SMRTPROPERTIES model with the inline form
class SMRTPROPERTIESAdmin(admin.ModelAdmin):
    inlines = [
        PropertyImageInline,
    ]



admin.site.register(SMRTPROPERTIES, SMRTPROPERTIESAdmin)
admin.site.register(SMRTWEBFORM)
admin.site.register(Asociados)