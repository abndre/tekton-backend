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
    telephone = models.CharField(max_length=200, default='', null=True)
    time_choice = (
        ("manha", "Manha"),
        ("tarde", "Tarde")
    )

    period = models.CharField(max_length=10, choices=time_choice, blank=False, null=False)
    city = models.CharField(max_length=200, default='', null=True)
    email = models.CharField(max_length=200, default='', null=True)

    def __str__(self):
        return self.name