from django.shortcuts import render

# Create your views here.
def construction(request):
    return render(request, 'Routers/construction.html')