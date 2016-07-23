# buglists/admin.py
from django.contrib import admin

from .models import Buglist, Tracker, Station


class StationInline(admin.TabularInline):
    model = Station
    extra = 1


@admin.register(Buglist)
class BuglistAdmin(admin.ModelAdmin):
    list_display = ['id','status', 'types', 'station', 'title', 'content', 'owner', 'created_at']
    inlines = [StationInline]

@admin.register(Tracker)
class BuglistAdmin(admin.ModelAdmin):
    list_display = ['id', 'buglist', 'message', 'owner', 'created_at']


@admin.register(Station)
class BuglistAdmin(admin.ModelAdmin):
    list_display = ['id', 'stationid', 'created_at']