from django.forms import ModelForm
from .models import AirPlay, Review, Track

class AirPlayForm(ModelForm):
    class Meta:
        model = AirPlay
        fields = ['date', 'segment']

class ReviewForm(ModelForm):
    class Meta: 
        model = Review
        fields = ['review']

class ReviewEditForm(ModelForm):
    class Meta: 
        model = Review
        fields = ['review']

class AddTrackForm(ModelForm):
    class Meta: 
        model = Track
        fields = ['title', 'number']

