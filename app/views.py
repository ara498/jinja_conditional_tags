from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':100,'b':200,'c':150}
    return render(request,'conditions.html',d)
