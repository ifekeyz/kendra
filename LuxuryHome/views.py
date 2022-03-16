from django.shortcuts import render

# Create your views here.
def luxury_homes(request):
    return render(request, 'routers/luxuryhomes.html')