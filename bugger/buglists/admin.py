# buglists/admin.py
from django.contrib import admin

from .models import Buglist


@admin.register(Buglist)
class BuglistAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']