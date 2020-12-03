from django.urls import path
from .views import (
    RouteDetailVeiw,
    RouteCreateVeiw,
    RouteUpdateVeiw,
    RouteDeleteView,
    UserRouteListView,
    AddressDetailView,
    AddressUpdateVeiw,
    AddressDeleteView,
    RouteAddressListView,
    SortedRouteListView
)
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('home/', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('test/', RouteAddressListView.as_view(), name='blog-test'),
    path('help/', views.help, name='blog-help'),
    path('route/<int:pk>/detail', RouteDetailVeiw.as_view(), name='route-detail'),
    path('route/new/', RouteCreateVeiw.as_view(), name='route-create'),
    path('route/<int:pk>/update', RouteUpdateVeiw.as_view(), name='route-update'),
    path('route/<int:pk>/delete', RouteDeleteView.as_view(), name='route-delete'),
    path('user/<str:username>/', UserRouteListView.as_view(), name='user-routes'),
    path('address/<int:pk>/', AddressDetailView.as_view(), name='address-detail'),
    path('address/new/', views.AddressCreateVeiw, name='address-create'),
    path('address/<int:pk>/update', AddressUpdateVeiw.as_view(), name='address-update'),
    path('address/<int:pk>/delete', AddressDeleteView.as_view(), name='address-delete'),
    path('route/<int:pk>/', RouteAddressListView.as_view(), name='route-addresses'),
    path('sorted-routes/', SortedRouteListView.as_view(), name='sorted-routes'),
    path('sort-addresses/', views.sort_addresses, name='sort-addresses'),

]

urlpatterns += staticfiles_urlpatterns()
