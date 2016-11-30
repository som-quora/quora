from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'frontpage/home.html', {})

def answer(request):
    return render(request, 'frontpage/answer.html', {})