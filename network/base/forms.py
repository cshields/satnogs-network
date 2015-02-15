from django import forms

from network.base.models import Station


class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ['name', 'image', 'alt',
                  'lat', 'lng', 'location', 'antenna', 'online']
        image = forms.ImageField(required=False)
