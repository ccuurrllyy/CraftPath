from blog.models import Address, Route
from django.contrib.auth.models import User
from mapwidgets.widgets import GooglePointFieldWidget
from django import forms
from django.contrib.gis.forms import PointField, ValidationError


class AddressCreationForm(forms.ModelForm):
    name = forms.CharField(required=True)
    location = PointField(widget=GooglePointFieldWidget(), required=True)
    route = forms.ModelChoiceField(queryset=Route.objects.all(), required=True)

    def clean(self):
        cleaned_data = super().clean()
        route = self.cleaned_data.get('route')
        make_initial_location = self.cleaned_data.get('make_initial_location')
        # Check if there is another address marked with initial location for this route
        if make_initial_location:
            route = Route.objects.get(pk=route.pk)
            if route.addresses.all().exclude(pk=self.instance.pk).filter(make_initial_location=True).exists():
                raise ValidationError("There is already an address marked as initial location.")
        return cleaned_data

    class Meta:
        model = Address
        fields = ('route', 'name', 'location', 'make_initial_location')
        widgets = {
            'location': GooglePointFieldWidget
        }

    def __init__(self, *args, **kwargs):
        super(AddressCreationForm, self).__init__(*args, **kwargs)
        try:
            if 'initial' in kwargs and 'user' in kwargs['initial']:
                routes = Route.objects.filter(username=kwargs['initial']['user'])
                self.fields['route'].queryset = routes
                self.fields['route'].initial = routes.first()
            elif 'instance' in kwargs:
                address = kwargs['instance']
                routes = Route.objects.filter(username=address.route.username)
                self.fields['route'].queryset = routes

        except Exception as e:
            print(e)
            pass
