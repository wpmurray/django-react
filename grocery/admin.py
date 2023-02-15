from django.contrib import admin
from .models import Grocery

class GroceryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

admin.site.register(Grocery, GroceryAdmin)
