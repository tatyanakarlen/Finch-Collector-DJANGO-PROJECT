from django.forms import ModelForm
from .models import AirPlay, Review

class AirPlayForm(ModelForm):
    class Meta:
        model = AirPlay
        fields = ['date', 'segment']

class ReviewForm(ModelForm):
    class Meta: 
        model = Review
        fields = ['review']

