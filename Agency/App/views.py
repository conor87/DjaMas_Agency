from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def opportunities(request):
    return render(request, 'opportunities.html')
