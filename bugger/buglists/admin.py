# buglists/admin.py
from django.contrib import admin

from .models import Buglist, Tracker


@admin.register(Buglist)
class BuglistAdmin(admin.ModelAdmin):
    list_display = ['id', 'types', 'title', 'content', 'owner', 'created_at']

@admin.register(Tracker)
class BuglistAdmin(admin.ModelAdmin):
    list_display = ['id', 'buglist', 'message', 'owner', 'created_at']