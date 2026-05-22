from django.db import models

class Employe(models.Model):
    nom = models.CharField(max_length=100)
    poste = models.CharField(max_length=100)
    salaire = models.DecimalField(max_digits=10, decimal_places=2)
    date_embauche = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nom