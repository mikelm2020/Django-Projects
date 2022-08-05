from django.shortcuts import render, HttpResponse

# Create your views here.
def store(request):
    return render(request, "store/store.html")