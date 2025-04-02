from django.contrib import admin
from .models import Activity
from django_summernote.admin import SummernoteModelAdmin

class ActivityAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(Activity,ActivityAdmin)