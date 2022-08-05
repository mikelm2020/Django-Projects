from django.shortcuts import render, HttpResponse

# Create your views here.
def services(request):
    return render(request,"services/services.html")