from django.core.exceptions import MultipleObjectsReturned
from django.http import Http404, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from blog.tools import get_best_path_and_cost
from .models import Route, Address, RouteBestPath, RouteBestPathLocation
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AddressCreationForm


def home(request):
    return render(request, 'blog/home.html', {'title': 'Home'})



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


class RouteCreateVeiw(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Route
    fields = ['title']
    # 'date_posted','number_of_locations']
    success_message = "Your route has been successfully created! You are now able to add locations!"

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class RouteUpdateVeiw(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
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
    success_url = '/blog/sorted-routes/'

    def test_func(self):
        route = self.get_object()
        if self.request.user == route.username:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def help(request):
    return render(request, 'blog/help.html', {'title': 'Help'})


class AddressDetailView(LoginRequiredMixin, DetailView):
    model = Address
    template_name = 'blog/address_detail.html'


@login_required
def AddressCreateVeiw(request):
    form = AddressCreationForm(initial={'user': request.user})
    if request.method == 'POST':
        form = AddressCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.username = request.user
            instance = form.save()
            messages.success(request, f'Your address has been successfully created!')
            return redirect(instance)
    return render(request, 'blog/address_form.html', {'form': form})


class AddressUpdateVeiw(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    form_class = AddressCreationForm
    model = Address
    success_message = "Your address has been successfully updated!"

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
    success_url = '/blog/sorted-routes/'

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
        var = get_object_or_404(Route, id=self.kwargs.get('pk'))
        # Initial location will appear first on the list
        addresses = Address.objects.filter(route=var).order_by('-make_initial_location', 'id')
        return addresses


class SortedRouteListView(LoginRequiredMixin, ListView):
    model = Route
    template_name = 'blog/sorted_routes.html'
    context_object_name = 'routes'
    ordering = ['-date_posted']
    paginate_by = 10

    def get_queryset(self):
        routes = Route.objects.filter(username=self.request.user, best_paths__isnull=False).order_by('id')
        return routes


class RouteBestPathLocations(object):
    pass


def sort_addresses(request):
    try:
        route_id = request.GET['route']
        route = Route.objects.get(pk=route_id)
    except Exception as e:
        print("Error", e)
        return JsonResponse({'success': False, 'message': 'Could not get Route'})

    # The Address marked with 'make_initial_location=True' will be location 1
    addresses = route.addresses.all().order_by('-make_initial_location', 'id')
    best_path, best_path_cost = get_best_path_and_cost(addresses) #returns best_path, cost_of_best_path
    best_path_list = [str(int(x)) for x in best_path]
    best_path_string = ', '.join(best_path_list)

    sorted_addresses = []
    for address_index in best_path_list:
        sorted_addresses.append(addresses[int(address_index) - 1])
    print(sorted_addresses)
    # Try to get existing object to update
    # Or create a new RouteBestPath
    try:
        route_best_path = RouteBestPath.objects.get(route=route_id)
        route_best_path.addresses.set(addresses)
        route_best_path.best_path_string = best_path_string
        route_best_path.best_path_cost = best_path_cost
        route_best_path.save()
        try:
            RouteBestPathLocation.objects.filter(route_best_path=route_best_path).delete()
        except:
            pass
        for pos, addr in enumerate(sorted_addresses): #enumerate is for loop with index
            RouteBestPathLocation.objects.create(route_best_path=route_best_path, address=addr, position=pos)
    except:
        route_best_path = RouteBestPath.objects.create(route=route, best_path_string=best_path_string,
                                                       best_path_cost=best_path_cost)
        route_best_path.addresses.set(addresses)
        for pos, addr in enumerate(sorted_addresses):
            RouteBestPathLocation.objects.create(route_best_path=route_best_path, address=addr, position=pos)

    return JsonResponse({'success': True,
                         'message': 'Sorting addresses is complete ✅. Check "Route Results " for the results of the algorithm.'})


