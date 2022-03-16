from django.shortcuts import render

# Create your views here.
def land_banking(request):
    return render(request, 'Routers/landbanking.html')