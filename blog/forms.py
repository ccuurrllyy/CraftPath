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
        form_route = self.cleaned_data.get('route')
        name = self.cleaned_data.get('name')
        make_initial_location = self.cleaned_data.get('make_initial_location')
        location = self.cleaned_data.get('location')

        # Check if location exists in this Route
        route = Route.objects.get(pk=form_route.pk)
        if location:
            if route.addresses.all().exclude(pk=self.instance.pk).filter(location=location).exists():
                raise ValidationError("There is already an address with this exact location. Please choose another location from the map.")
        else:
            raise ValidationError("Please choose a location from the map.")

        # Check if there is another address marked with initial location for this route
        if make_initial_location:
            if route.addresses.all().exclude(pk=self.instance.pk).filter(make_initial_location=True).exists():
                raise ValidationError("There is already an address marked as initial location.")

        # Check if address with the same name has been added before
        if name:
            if route.addresses.all().exclude(pk=self.instance.pk).filter(name=name).exists():
                raise ValidationError("There is already an address with that name in your route.")
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
