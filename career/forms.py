from django import forms

from .models import Coordinate


class CoordinateForm(forms.ModelForm):

    class Meta:
        model = Coordinate
        fields = ['x_coordinate', 'y_coordinate']
