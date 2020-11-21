from django import forms
from blog.models import Address, Area

class AddressCreationForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['route_name','name', 'city','area']
            # ,'make_initial_location']

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['area'].queryset = Area.objects.none()

        if 'city' in self.data:
            try:
                city_id = int(self.data.get('city'))
                self.fields['area'].queryset = Area.objects.filter(city_id=city_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['area'].queryset = self.instance.city.area_set.order_by('name')

