from django.shortcuts import render

def F(request):
    return render(request, 'F/far.html', {'age':2})

def urmi(request):
    return render(request, 'F/uf.html', {'age':22})
