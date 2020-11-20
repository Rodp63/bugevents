from django.contrib import admin

from .models import Ambiente, Evento, Actividad, Ponente, Turno, Material, Catalogo, Item
from .forms import AmbienteForm, EventoForm, TurnoForm, ActividadForm, ItemForm


class AmbienteAdmin(admin.ModelAdmin):
    form = AmbienteForm
admin.site.register(Ambiente, AmbienteAdmin)


class ActividadInline(admin.TabularInline):
    model = Actividad
    form = ActividadForm
    show_change_link = True


class EventoAdmin(admin.ModelAdmin):
    form = EventoForm
    inlines = [ActividadInline]
admin.site.register(Evento, EventoAdmin)


admin.site.register(Ponente)


class TurnoAdmin(admin.ModelAdmin):
    form = TurnoForm

    def get_model_perms(self, request):
        return {}
admin.site.register(Turno, TurnoAdmin)


class TurnoInline(admin.TabularInline):
    model = Turno
    show_change_link = True


class ActividadAdmin(admin.ModelAdmin):
    model = Actividad
    form = ActividadForm
    inlines = [TurnoInline]

    def get_model_perms(self, request):
        return {}
admin.site.register(Actividad, ActividadAdmin)


admin.site.register(Material)


class ItemInline(admin.TabularInline):
    model = Item
    form = ItemForm
    show_change_link = True

    
class CatalogoAdmin(admin.ModelAdmin):
    inlines  = [ItemInline]
admin.site.register(Catalogo, CatalogoAdmin)
