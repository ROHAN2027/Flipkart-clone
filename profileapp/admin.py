from django.contrib import admin
from .models import profile
# Register your models here.
# class profileadmin(admin.ModelAdmin):
#     list_display = ('name', 'email')

admin.site.register(profile)