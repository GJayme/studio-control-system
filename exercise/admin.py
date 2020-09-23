from django.contrib import admin

from exercise.models import Exercicio


@admin.register(Exercicio)
class ExercicioAdmin(admin.ModelAdmin):
    list_display = ['name', 'muscle_group']
    fields = ('name', 'muscle_group')
    search_fields = ('name', 'muscle_group')
