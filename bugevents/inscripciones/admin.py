from django.contrib import admin

from .models import Paquete, Promocion, TipoParticipante
from .forms import PaqueteForm, PromocionForm


class PromocionInline(admin.TabularInline):
    model = Promocion
    form = PromocionForm
    show_change_link = True


class PaqueteAdmin(admin.ModelAdmin):
    model = Paquete
    form = PaqueteForm
    inlines = [PromocionInline]
admin.site.register(Paquete, PaqueteAdmin)
