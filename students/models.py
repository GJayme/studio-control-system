from django.db import models


class Aluno(models.Model):
    male = "Masculino"
    female = "Feminino"
    GENDER_CHOICES = [
        (male, "Masculino"),
        (female, "Feminino"),
    ]

    name = models.CharField(max_length=255)
    date_of_birthday = models.DateField(auto_now_add=False, auto_now=False)
    telephone = models.CharField(max_length=11)
    email = models.EmailField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, default=female)
    address = models.CharField(max_length=255)
