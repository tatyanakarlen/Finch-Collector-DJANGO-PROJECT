from django.forms import ModelForm
from .models import AirPlay

class AirPlayForm(ModelForm):
    class Meta:
        model = AirPlay
        fields = ['date', 'segment']

