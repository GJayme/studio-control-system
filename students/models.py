from django.db import models

class Aluno(models.Model):
  name = models.CharField(max_length=255)
  
