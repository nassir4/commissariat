from django.forms import ModelForm

from secretariat.models import Gallerie, ImagePot


class GallerieForm(ModelForm):
    class Meta:
        model=Gallerie
        fields=['titre','image','description']
class ImagePotForm(ModelForm):
    class Meta:
        model = ImagePot
        fields =['image']