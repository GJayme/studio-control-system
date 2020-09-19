from django.contrib import admin

from .models import Aluno, Anamnese


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'gender']
    fields = ('name', 'date_of_birthday', 'telephone',
              'email', 'cpf', 'gender', 'address')


@admin.register(Anamnese)
class Anamnese(admin.ModelAdmin):
    list_display = ['weight', 'height', 'imc']
    fields = ('weight', 'height', 'imc', 'has_pathology',
              'pathology', 'use_medicine', 'medicine', 'has_surgery',
              'surgery', 'heart_rate', 'objective', 'has_physical_activity',
              'physical_activity', 'sleep_hours', 'has_smoker', 'meals_day')
