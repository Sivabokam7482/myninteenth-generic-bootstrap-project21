from django.shortcuts import render

# Create your views here.
def cdnmethod(request):
    return render(request,'cdn.html')


def downloadmethod(request):
    return render(request,'download.html')
    
    
