from django.contrib import admin
from .models import Bonds

admin.site.register(Bonds)
# class AuthorAdmin(admin.ModelAdmin):
#     fields = ['__all__']


admin.site.site_header = "Backend Challenge"
admin.site.site_title = "Backend Challenge"
admin.site.index_title = "Admin Panel for Backend Challenge"