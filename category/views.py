from django.shortcuts import render

def hello(request):
    return render(request, 'hello.html')

def about(request):
    return render(request, 'pages/apropos.html')

def index(request):
    return render(request, 'pages/index.html')

def horaire(request):
    return render(request, 'pages/timeline.html')

def revu(request):
    return render(request, 'pages/reviews.html')

def reserver(request):
    return render(request, 'pages/booking.html')

def info(request):
    return render(request, 'pages/learnn.html')

# Create your views here.
