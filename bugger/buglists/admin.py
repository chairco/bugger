# buglists/admin.py
from django.contrib import admin

from .models import Buglist, Tracker


@admin.register(Buglist)
class BuglistAdmin(admin.ModelAdmin):
    list_display = ['types', 'title', 'content']

@admin.register(Tracker)
class BuglistAdmin(admin.ModelAdmin):
    list_display = ['buglist', 'message', 'created_at']