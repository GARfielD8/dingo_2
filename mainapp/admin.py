from django.contrib import admin
from .models import *
from django.utils.html import format_html


# Register your models here.
class FoodAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class BookingAdmin(admin.ModelAdmin):
    list_display = ('fname', 'time', 'numbers', 'persons')

class ChefAdmin(admin.ModelAdmin):
    list_display = ('fname', 'position', 'image')

    def image(self, obj):
        return format_html('<img src="{}"/>'.format(obj.image.url))

admin.site.register(FoodModel, FoodAdmin)
admin.site.register(Category)
admin.site.register(WorkersModels)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Feedback)
