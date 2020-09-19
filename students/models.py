from django.db import models

from django.core.exceptions import ValidationError


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

    def __str__(self):
        return "O aluno {} foi cadastrado!".format(self.name)


class Anamnese(models.Model):
    wigth_loss = "Emagrecimento"
    hypertrophy = "Hipertrofia"
    muscle_strengthening = "Fortalecimento"
    muscle_endurance = "Resistência"
    muscle_strength = "Força"
    OBJECTIVE_CHOICES = [
        (wigth_loss, "Emagrecimento"),
        (hypertrophy, "Hipertrofia"),
        (muscle_strengthening, "Fortalecimento"),
        (muscle_endurance, "Resistência"),
        (muscle_strength, "Força")
    ]
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    imc = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    has_pathology = models.BooleanField(default=False)
    pathology = models.TextField(null=True, blank=True)
    use_medicine = models.BooleanField(default=False)
    medicine = models.TextField(null=True, blank=True)
    has_surgery = models.BooleanField(default=False)
    surgery = models.TextField(null=True, blank=True)
    heart_rate = models.DecimalField(max_digits=5, decimal_places=2)
    objective = models.CharField(
        max_length=20, choices=OBJECTIVE_CHOICES, default=wigth_loss)
    has_physical_activity = models.BooleanField(default=False)
    physical_activity = models.TextField(null=True, blank=True)
    sleep_hours = models.DecimalField(max_digits=5, decimal_places=2)
    has_smoker = models.BooleanField(default=False)
    meals_day = models.IntegerField()

    def __str__(self):
        return "Anamnese cadastrada!"

    def save(self, *args, **kwargs):
        self.clean()
        return super(Anamnese, self).save(*args, **kwargs)

    def clean(self):
        try:
            weight = self.weight
            height = self.height
            imc = (weight/(height)**2)*10000

            self.imc = imc
            print(self.imc)
            super(Anamnese, self).clean()
        except:
            raise ValidationError("Erro ao calcular o IMC!")
