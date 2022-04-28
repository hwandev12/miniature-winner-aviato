from django.shortcuts import render

def display(request):
    return render(request, 'pages/index.html')
