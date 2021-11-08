from django.db import models


# Create your models here.
class Professional(models.Model):
    name = models.CharField(max_length=200)
    ability_choice = (
        ("pedreiro", "Pedreiro"),
        ("pintor", "Pintor"),
        ("encacanador", "Encanador")
    )

    ability = models.CharField(max_length=100, choices=ability_choice, blank=False, null=False)

    def __str__(self):
        return self.name