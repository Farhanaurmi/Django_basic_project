from django.shortcuts import render

def Mu(request):
    return render(request, 'M/mo.html', {'age':6})

    
