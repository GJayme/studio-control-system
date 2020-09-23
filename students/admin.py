from django.contrib import admin

from students.models import Aluno


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'gender']
    fields = ('name', 'date_of_birthday', 'telephone',
              'email', 'cpf', 'gender', 'address', 'weight', 'height',
              'has_pathology',
              'pathology', 'use_medicine', 'medicine', 'has_surgery',
              'surgery', 'heart_rate', 'objective', 'has_physical_activity',
              'physical_activity', 'sleep_hours', 'has_smoker', 'meals_day')
    search_fields = ('name', 'email')
