from django.contrib import admin
from .models import *
from django.contrib import admin
from . import models

admin.site.site_header = "Text Game Admin"

@admin.display(description="Here is name of rooms'author")
def upper_case_author_name(obj):
    return obj.author.username.upper()




class MainappAdmin(admin.ModelAdmin):
    list_display_links = ['room_name']
    list_display = ['room_name', upper_case_author_name, 'type', 'create_date']
    search_fields = ['room_name', 'room_author_name']
    search_help_text = 'Enter search query'
    show_full_result_count = False

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            path_t = f"{BASE_DIR}/chat/chats_data/{obj.pk}.txt"
            path_a = f"{BASE_DIR}/chat/actions_data/{obj.pk}.txt"
            remove(path_t)
            remove(path_a)
        queryset.delete()

admin.site.register(Rooms, MainappAdmin)

# Register your models here.
