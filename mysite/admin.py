from django.contrib import admin
from mysite.models import Update

class UpdateAdmin(admin.ModelAdmin):
    pass

admin.site.register(Update, UpdateAdmin)