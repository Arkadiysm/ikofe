from django.contrib import admin
from .models import Event, Project, pageHit


@admin.register(pageHit)
class PageHit(admin.ModelAdmin):
    readonly_fields = ['title', 'count']


admin.site.register(Event)
admin.site.register(Project)



