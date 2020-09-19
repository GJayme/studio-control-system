from django.contrib import admin

from .models import Aluno


@admin.register(Aluno)
class ALunoAdmin(admin.ModelAdmin):
    fields = ('name', 'date_of_birthday', 'telephone',
              'email', 'cpf', 'gender', 'address')
