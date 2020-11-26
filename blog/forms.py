from blog.models import Address, Area
from mapwidgets.widgets import GooglePointFieldWidget
from django import forms
from django.contrib.gis.forms import PointField


class AddressCreationForm(forms.ModelForm):
    name = forms.CharField(required=True)
    location = PointField(widget=GooglePointFieldWidget(), required=True)

    class Meta:
        model = Address
        fields = ('route', 'name', 'location', 'make_initial_location')
        widgets = {
            'location': GooglePointFieldWidget
        }