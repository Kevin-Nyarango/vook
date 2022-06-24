from re import search
from django.contrib import admin

from .models import Project, TechStack, Contact



class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('tech_stacks',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ('tech_stacks',)


admin.site.register(Project, ProjectAdmin)


class TechStackAdmin(admin.ModelAdmin):
    search_fields = ('name',)


admin.site.register(TechStack, TechStackAdmin)



class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'created')
    list_filter = ('created',)
    search_fields = ('message',)


admin.site.register(Contact, ContactAdmin)