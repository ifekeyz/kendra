from django.shortcuts import render

# Create your views here.
def property_development(request):
    return render(request, 'routers/propertymanagement.html')
