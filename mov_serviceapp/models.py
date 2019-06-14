from django.db import models
import datetime


class Film(models.Model):
    naziv = models.CharField(max_length=30)
    zanr = models.CharField(max_length=10)
    glumci = models.CharField(max_length=150)
    vreme_trajanja = models.DurationField()



class Projekcija(models.Model):

    IMA_MESTA = 'IM'
    POPUNJENO = 'POP'

    STATUS_CHOICES = (
        ( IMA_MESTA , 'Ima Mesta'),
        (POPUNJENO , 'Popunjeno')
    )


    film = models.CharField(max_length=150)
    vreme_pocetka = models.DateTimeField()
    sala = models.IntegerField()
    cena_karte = models.IntegerField()
    status = models.CharField(
        max_length=2,
        choices= STATUS_CHOICES,default=IMA_MESTA,


    )


class Sala(models.Model):
    broj_sale = models.IntegerField()
    broj_redova = models.IntegerField()
    broj_sedista_red = models.IntegerField()


