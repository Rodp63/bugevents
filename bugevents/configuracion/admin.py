from django.contrib import admin

from .models import Ambiente, Evento, Actividad, Ponente, Turno, Material
from .forms import AmbienteForm, EventoForm, TurnoForm, MaterialForm


class AmbienteAdmin(admin.ModelAdmin):
    form = AmbienteForm
admin.site.register(Ambiente, AmbienteAdmin)


class ActividadInline(admin.TabularInline):
    model = Actividad
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


class MaterialAdmin(admin.ModelAdmin):
    form = MaterialForm
admin.site.register(Material,MaterialAdmin)


class TurnoInline(admin.TabularInline):
    model = Turno


class ActividadAdmin(admin.ModelAdmin):
    model = Actividad
    inlines = [TurnoInline]

    def get_model_perms(self, request):
        return {}


admin.site.register(Actividad, ActividadAdmin)