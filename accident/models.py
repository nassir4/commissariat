from bootstrap_datepicker_plus import DatePickerInput
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# # # # # # # # # # # # # # # # # # # # #

# MODELS ACCIDENT CORPOREL

# # # # # # # # # # # # # # # # # # # # #

# models type accident
class TypeAccident(models.Model):
    nom = models.CharField("Nom", max_length=200, unique=True)
    description = models.TextField("Description", blank=True)

    def __str__(self):
        return self.nom


# models section accident
class Accident(models.Model):
    numero_accident = models.CharField("Numero", max_length=255)
    date_accident = models.DateField("Date", auto_now_add=False)
    heure_accident = models.TimeField("Heure", auto_now_add=False)
    lieu_accident = models.CharField("Lieu", max_length=255)
    type_accident = models.ForeignKey(TypeAccident, on_delete=models.CASCADE ,blank=True,null=True)
    etabli_par = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accident_etablie")
    assiste_de = models.ManyToManyField(User)
    mesures_prises = models.TextField("Mesures Prises", null=True, blank=True)
    circonstances = models.TextField("Circonstances", null=True, blank=True)
    infractions_relevees = models.TextField("Infractions Relevees", null=True, blank=True)
    derniere_mesures_prises = models.TextField("Derniere Mesures Prises", null=True, blank=True)
    autres_dommages = models.TextField("Autres dommages causes par l'accident", null=True, blank=True)

    def __str__(self):
        return f'{self.numero_accident}-{self.lieu_accident}'


# models vehicule
class Vehicule(models.Model):
    numero = models.CharField("Numero", max_length=200)
    genre = models.CharField("Genre", max_length=255)
    marque = models.CharField("Marque", max_length=255)
    puissance = models.CharField("Puissance", max_length=255,blank=True)
    charge_total = models.CharField("Charge Total", max_length=255,blank=True)
    dimension = models.CharField("Dimension", max_length=255,blank=True)
    date_mise_circulation = models.DateField("Date de mise en circulation", auto_now_add=False)
    derniere_visite_technique = models.DateField("Derniere visite technique", auto_now_add=False)
    kilometrage = models.CharField("Kilometrage", max_length=255, blank=True)
    etat_general = models.TextField("Etat general", blank=True)
    valeur_systeme_freinage = models.CharField("Valeur du systeme de freinage",blank=True ,max_length=255)
    etat_pneus_avant = models.TextField("Etat des pneus avant",blank=True)
    etat_pneus_arriere = models.TextField("Etat des pneus arriere", blank=True)
    etat_parebrise = models.TextField("Etat du parebrise",blank=True)
    position_levier_vitesse = models.TextField("Position du levier de changement de vitesse",blank=True)
    presence_poste_radio = models.BooleanField("Presence d'un poste radio", default=True,blank=True)
    degats_materiels = models.TextField("Degats materiels", blank=True)
    accident = models.ForeignKey(Accident, on_delete=models.CASCADE ,blank=True,null=True)

    def __str__(self):
        return f'{self.numero}-{self.marque}'


# models eclairage
class Eclairage(models.Model):
    vehicule = models.OneToOneField(Vehicule, on_delete=models.CASCADE,blank=True,null=True)
    existance = models.BooleanField("Existance", default=True)
    fonctionel = models.BooleanField("Fonctionel", default=True)
    position = models.BooleanField("Position", default=True)

    def __str__(self):
        return self.vehicule.numero


# models avertisseur
class Avertisseur(models.Model):
    vehicule = models.OneToOneField(Vehicule, on_delete=models.CASCADE,blank=True,null=True)
    existance = models.BooleanField("Existance", default=True)
    fonctionel = models.BooleanField("Fonctionel", default=True)
    position = models.BooleanField("Position", default=True)

    def __str__(self):
        return self.vehicule.numero


# models Indicateur de direction
class IndicateurDirection(models.Model):
    vehicule = models.OneToOneField(Vehicule, on_delete=models.CASCADE,blank=True,null=True)
    existance = models.BooleanField("Existance", default=True)
    fonctionel = models.BooleanField("Fonctionel", default=True)
    position = models.BooleanField("Position", default=True)

    def __str__(self):
        return self.vehicule.numero


# models indicateur de vitesse
class IndicateurVitesse(models.Model):
    vehicule = models.OneToOneField(Vehicule, on_delete=models.CASCADE,blank=True,null=True)
    existance = models.BooleanField("Existance", default=True)
    fonctionel = models.BooleanField("Fonctionel", default=True)
    position = models.BooleanField("Position", default=True)

    def __str__(self):
        return self.vehicule.numero


# models essuie glace
class EssuieGlace(models.Model):
    vehicule = models.OneToOneField(Vehicule, on_delete=models.CASCADE,blank=True,null=True)
    existance = models.BooleanField("Existance", default=True)
    fonctionel = models.BooleanField("Fonctionel", default=True)
    position = models.BooleanField("Position", default=True)

    def __str__(self):
        return self.vehicule.numero


# models indicateur de vitesse
class Retroviseur(models.Model):
    vehicule = models.OneToOneField(Vehicule, on_delete=models.CASCADE,blank=True,null=True)
    existance = models.BooleanField("Existance", default=True)
    fonctionel = models.BooleanField("Fonctionel", default=True)
    position = models.BooleanField("Position", default=True)

    def __str__(self):
        return self.vehicule.numero


# models Conducteur
class Conducteur(models.Model):
    nom_prenom = models.CharField("Nom & Prenom", max_length=255)
    date_naissance = models.DateField("Date de naissance", blank=True, null=True, auto_now_add=False)
    lieu_naissance = models.CharField("Lieu de naissance",blank=True, max_length=255)
    filiation = models.CharField("Filiation",blank=True, max_length=255)
    profession = models.CharField("Profession", max_length=255)
    domicile = models.CharField("Domicile",blank=True, max_length=255)
    telephone = models.CharField("Telephone",blank=True, max_length=15)
    comportement = models.CharField("Comportement",blank=True, max_length=200)
    vehicule = models.OneToOneField(Vehicule, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.nom_prenom


# models proprietaire
class Proprietaire(models.Model):
    nom_prenom = models.CharField("Nom & Prenom", max_length=255)
    domicile = models.CharField("Domicile", max_length=255)
    vehicule = models.OneToOneField(Vehicule, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.nom_prenom


# modele permis
class Permis(models.Model):
    numero = models.CharField("Numero", max_length=200)
    delivre_par = models.CharField("Delivre par", max_length=200)
    delivre_le = models.DateField("Delivre le", auto_now_add=False)
    lieu = models.CharField("Lieu", max_length=255)
    conducteur = models.OneToOneField(Conducteur, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f'Permis => {self.conducteur.nom_prenom}'


# models assurance
class Assurance(models.Model):
    nom = models.CharField("Nom", max_length=255)
    numero_police = models.CharField("Numero police", max_length=200)
    date_debut = models.DateField("Date debut", auto_now_add=False)
    date_expiration = models.DateField("Date d'expiration", auto_now_add=False)
    vehicule = models.OneToOneField(Vehicule, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f'Assurance => {self.vehicule}'


# models vignette
class Vignette(models.Model):
    vehicule = models.OneToOneField(Vehicule, on_delete=models.CASCADE,blank=True,null=True)
    pass


# models victime
class Victime(models.Model):
    nom_prenom = models.CharField("Nom & Prenom", max_length=255)
    filiation_complete = models.CharField("Filiation complete", max_length=255)
    adresse = models.CharField("Adresse", max_length=255)
    nature_des_blessures = models.TextField("Nature des blessures")
    position_moment_accident = models.CharField("Position au moment de l'accident", max_length=255)
    accident = models.ForeignKey(Accident, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.nom_prenom


# models temoin
class Temoin(models.Model):
    nom_prenom = models.CharField("Nom & Prenom", max_length=255)
    profession = models.CharField("Profession", max_length=255)
    adresse = models.CharField("Adresse", max_length=255)
    position_moment_accident = models.CharField("Position au moment de l'accident", max_length=255)
    accident = models.ForeignKey(Accident, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.nom_prenom


# models etat des lieux
class EtatDesLieux(models.Model):
    visibilite = models.CharField("Visibilite", max_length=255)
    chaussee = models.CharField("Chausse", max_length=255)
    largeur = models.CharField("Largeur", max_length=255)
    eclairage = models.CharField("Eclairage", max_length=255)
    tracesFreinage = models.CharField("Traces de freinage", max_length=255)
    tracesSang = models.CharField("Traces de sang", max_length=255)
    tracePneu = models.CharField("Traces de pneus", max_length=255)
    PassagePieton = models.CharField("Passage pieton", max_length=255)
    condition_atmospherique = models.TextField("Conditions atmospheriques")
    accident = models.OneToOneField(Accident, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f'Etat des lieux numero: {self.id}'


# # # # # # # # # # # # # # # # # # # # #

# MODELS ACCIDENT MATERIEL

# # # # # # # # # # # # # # # # # # # # #

# modls declaration
class Declaration(models.Model):
    conducteur = models.OneToOneField(Conducteur, on_delete=models.CASCADE,blank=True,null=True)
    declaration = models.TextField("Declaration")
    infraction = models.TextField("Infraction", null=True, blank=True)

    def __str__(self):
        return self.conducteur
