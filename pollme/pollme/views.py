from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'home.html', context)

def submit(requst):
    return render(requst, 'submitpage.html')

