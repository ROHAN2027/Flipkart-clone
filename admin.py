from django.contrib import admin
from info.models import info

class infoadmin(admin.ModelAdmin):
    list_display = ('name', 'email')

admin.site.register(info, infoadmin)

# Register your models here.
