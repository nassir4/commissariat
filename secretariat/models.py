from django.db import models

# Create your models here.
class Gallerie(models.Model):
    titre = models.CharField("Titre", max_length=255)
    description = models.TextField("Description", max_length=255)
    image = models.ImageField(upload_to='galleries/')
    dateCreation = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.description}-->{self.dateCreation}'
class ImagePot(models.Model):
    gallerie = models.ForeignKey(Gallerie, verbose_name="Cérémonie", on_delete=models.CASCADE,)
    image = models.ImageField(upload_to='galeries/')
    dateCreation = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.image.url}'