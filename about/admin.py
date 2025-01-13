from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    registers the About model against the admin site
    and applies the Summernote features below through to the model
    """
    summernote_fields = ('content',)