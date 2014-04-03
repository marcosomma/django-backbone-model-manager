from django.shortcuts import render

# Create your views here.
def coursePage(request):
    return render(request, 'home.html')
