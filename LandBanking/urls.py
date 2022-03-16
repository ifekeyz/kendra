from django.urls import path

from .import views

urlpatterns = [
    path('land_banking/',views.land_banking, name='land_banking'),
]