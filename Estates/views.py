from django.shortcuts import render

# Create your views here.
def estates(request):
    return render(request, 'routers/Estates.html')
