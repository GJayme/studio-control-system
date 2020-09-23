from django.db import models


class Exercicio(models.Model):
  # Muscle Group Choices
    quadriceps = "Quadríceps"
    dorsal = "Dorsal"
    back_haunch = "Posterior de Coxa"
    chest = "Peitoral"
    biceps = "Bíceps"
    triceps = "Tríceps"
    shoulder = "Ombro"
    abdomen = "Abdômen"
    calf = "Panturrilha"
    cardio = "Cardio"
    EXERCISE_CHOICES = [
        (quadriceps, "Quadríceps"),
        (dorsal, "Dorsal"),
        (back_haunch, "Posterior de Coxa"),
        (chest, "Peitoral"),
        (biceps, "Bíceps"),
        (triceps, "Tríceps"),
        (shoulder, "Ombro"),
        (abdomen, "Abdômen"),
        (calf, "Panturrilha"),
        (cardio, "Cardio"),
    ]

  # Objective Group Choices
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

    name = models.CharField(max_length=255)
    muscle_group = models.CharField(max_length=20, choices=EXERCISE_CHOICES)

    def __str__(self):
        return self.name
