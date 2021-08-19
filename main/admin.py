from django.contrib import admin
from .models import Corporation, TeamMember, Work

class WorkAdmin(admin.ModelAdmin):
    list_display = ('work_name', 'displayOnLandingPage')

class CorpAdmin(admin.ModelAdmin):
    list_display = ('corp_name',)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('member_name', 'member_job')

admin.site.register(Corporation, CorpAdmin)
admin.site.register(TeamMember, TeamAdmin)
admin.site.register(Work, WorkAdmin)
