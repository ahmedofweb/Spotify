from django.contrib.auth.models import User
from django.db import models

class Qoshiqchi(models.Model):
    ism = models.CharField(max_length=50)
    tugilgan_yil = models.DateField()
    davlat = models.CharField(max_length=50)
    def __str__(self):
        return self.ism

class Albom(models.Model):
    nom = models.CharField(max_length=100)
    sana = models.DateField()
    rasm = models.FileField(blank=True, null=True)
    qoshiqchi = models.ForeignKey(Qoshiqchi, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Qoshiq(models.Model):
    nom = models.CharField(max_length=50)
    janr = models.CharField(max_length=50)
    davomiylik = models.PositiveSmallIntegerField(blank=True, null=True)
    fayl = models.FileField(blank=True, null=True)
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Izoh(models.Model):
    matn = models.CharField(max_length=150)
    sana = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.matn
