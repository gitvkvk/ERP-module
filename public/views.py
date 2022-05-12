from django.shortcuts import render

def indexpublic(request):
    return render(request, 'indexpublic.html')

def careers(request):
    return render(request, 'careers.html')

def projects(request):
    return render(request, 'projects.html')

def contactus(request):
    return render(request, 'contactus.html')