from django.urls import path

from .import views

urlpatterns = [
    path('real_estate_school',views.real_estate_school, name='real_estate_school'),
]