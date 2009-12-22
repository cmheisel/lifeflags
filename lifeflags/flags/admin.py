from django.contrib import admin

from lifeflags.flags.models import Flag

class FlagAdmin(admin.ModelAdmin):
    exclude = ("slug", )
    list_display = ('offense', 'players', 'slug')
admin.site.register(Flag, FlagAdmin)
