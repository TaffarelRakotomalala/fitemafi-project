from django.db import models
from django.contrib.auth.models import User

adresse_membres = (
    ('Interne', 'Interne'),
    ('Externe', 'Externe'),
)

class Membres(models.Model):
    nom = models.CharField(max_length = 30, verbose_name = "Nom")
    prenoms = models.CharField(max_length = 50, verbose_name = "Prénoms")
    adresse = models.CharField(max_length = 10, choices = adresse_membres, default = 'Interne')

    def __str__(self):
        return (str(self.id) + " " + self.nom + " " + self.prenoms)

class Droit(models.Model):
    id_droit = models.DateTimeField(primary_key=True ,auto_now=True)
    droit_adhension = models.BooleanField(help_text=u'Payé?', default=False, unique = False, verbose_name="Droit d'adhension")
    droit_annuel = models.BooleanField(help_text=u'Payé?', default=False, unique = False, verbose_name="Droit Annuel")
    droit_reception = models.BooleanField(help_text=u'Payé?', default=False, unique = False, verbose_name="Droit de réception")
    id_membres = models.ForeignKey(Membres, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.id_membres)

class Utilisateur(models.Model):
    proprietaire = models.OneToOneField(User, on_delete = models.CASCADE)
    avatar = models.ImageField(null = True, blank = True, verbose_name = 'avatar', default = 'profil.png')

    def __unicode__(self):
        return self.proprietaire


