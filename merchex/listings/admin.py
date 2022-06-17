from django.contrib import admin

from listings.models import Band
from listings.models import Title


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')


class TitleAdmin(admin.ModelAdmin):
    list_display = ('name_title', 'type', 'sold', 'band')


admin.site.register(Band, BandAdmin)
admin.site.register(Title, TitleAdmin)
