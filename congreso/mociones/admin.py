from django.contrib import admin

from mociones.models import Mocion, Categoria


class MocionAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'contenido',)
    list_display = ('nombre', 'categoria', 'estado',)
    list_display_links = list_display
    list_filter = ('categoria', 'estado',)


admin.site.register(Mocion, MocionAdmin)
admin.site.register(Categoria)
