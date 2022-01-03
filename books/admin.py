from django.contrib import admin
from .models import book
# Register your models here.

class bookAdmin(admin.ModelAdmin):
    list_display=('book_name','book_id','author')

admin.site.register(book,bookAdmin)