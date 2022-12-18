from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")
def removepunc(request):
    djtext=request.GET.get('text')
    analyze=djtext.upper()

    params={'removetext':analyze}
    return render(request,"removepunc.html",params)
