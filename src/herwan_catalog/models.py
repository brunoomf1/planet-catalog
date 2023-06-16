from django.db import models

class Planeta(models.Model):
    nome = models.CharField(max_length=100)
    # Outros campos do modelo, se houver

    def __str__(self):
        return self.nome