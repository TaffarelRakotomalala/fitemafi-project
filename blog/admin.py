from django.contrib import admin
from blog.models import Membres, Droit, Utilisateur


class MembresAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenoms', 'adresse',)
    list_filter = ('adresse', 'nom')
    search_fields = ('nom',)
    ordering = ('id',)

class DroitAdmin(admin.ModelAdmin):
    list_display = ('id_droit', 'id_membres', 'droit_adhension', 'droit_annuel', 'droit_reception')
    list_filter = ('id_membres',)
    search_fields = ('id_membres',)
    ordering = ('id_membres',)

admin.site.register(Droit, DroitAdmin)
admin.site.register(Membres, MembresAdmin)
admin.site.register(Utilisateur)
