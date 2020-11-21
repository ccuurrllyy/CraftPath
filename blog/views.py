from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Route, Address,Area
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
def home(request):
    return render(request, 'blog/home.html', {'title': 'Home'})


class RouteListView(LoginRequiredMixin, ListView):
    model = Route
    template_name = 'blog/main.html'
    context_object_name = 'routes'
    ordering = ['-date_posted']
    paginate_by = 20


class UserRouteListView(LoginRequiredMixin, ListView):
    model = Route
    template_name = 'blog/user_routes.html'
    context_object_name = 'routes'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Route.objects.filter(username=user).order_by('-date_posted')


class RouteDetailVeiw(LoginRequiredMixin, DetailView):
    model = Route


class RouteCreateVeiw(LoginRequiredMixin,SuccessMessageMixin, CreateView):
    model = Route
    fields = ['title']
    # 'date_posted','number_of_locations']
    success_message = "Your route has been successfully created! You are now able to add locations!"

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class RouteUpdateVeiw(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,UpdateView):
    model = Route
    fields = ['title']
    # 'date_posted','number_of_locations']
    success_message = "Your route has been successfully updated!"

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)
    def test_func(self):
        route = self.get_object()
        if self.request.user == route.username:
            return True
        return False



class RouteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Route
    success_url = '/blog/main/'

    def test_func(self):
        route = self.get_object()
        if self.request.user == route.username:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def help(request):
    return render(request, 'blog/help.html', {'title': 'Help'})




class AddressListView(LoginRequiredMixin, ListView):
    model = Address
    template_name = 'blog/addresses.html'
    context_object_name = 'addresses'
    paginate_by = 10


class AddressDetailView(LoginRequiredMixin, DetailView):
    model = Address
    template_name = 'blog/address_detail.html'


from .forms import AddressCreationForm
@login_required
def AddressCreateVeiw(request):
    form = AddressCreationForm()
    if request.method == 'POST':
        form = AddressCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.username = request.user
            instance = form.save()
            messages.success(request, f'Your address has been successfully created!')
            return redirect(instance)
    return render(request, 'blog/address_form.html', {'form': form})

class AddressUpdateVeiw(LoginRequiredMixin, UserPassesTestMixin,SuccessMessageMixin, UpdateView):
    model = Address
    fields = [ 'route_name','name', 'city','area',]
    success_message = "Your address has been successfully added!"

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def test_func(self):
        address = self.get_object()
        if self.request.user == address.username:
            return True
        return False

class AddressDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Address
    success_url = '/blog/main/'

    def test_func(self):
        address = self.get_object()
        if self.request.user == address.username:
            return True
        return False

class RouteAddressListView(LoginRequiredMixin, ListView):
    model = Address
    template_name = 'blog/route_addresses.html'
    context_object_name = 'addresses'
    paginate_by = 100

    def get_queryset(self):
        var = get_object_or_404(Route,title=self.kwargs.get('route_name'))
        return Address.objects.filter(route_name=var)

# AJAX
def load_areas(request):
    city_id = request.GET.get('city_id')
    areas = Area.objects.filter(city_id=city_id).all()
    return render(request,'blog/area_dropdown_list_options.html', {'areas': areas})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)