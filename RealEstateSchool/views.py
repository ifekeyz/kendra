from django.shortcuts import render

# Create your views here.
def real_estate_school(request):
    return render(request, 'routers/school_of_sales.html')