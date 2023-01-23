from django.shortcuts import render, HttpResponse

# Create your views here.
def test(request):
    return HttpResponse("<H1>Hello World <br> This is My World Wide Web </H1>")

def home(request):
    return render(request, 'home.html')
def record(request):
    return render(request, 'record.html')
def firstweb(request):
    return render(request, 'firstweb.html')
def secondpage(request):
    return render(request, 'secondpage.html')
def thirdpage(request):
    return render(request, 'thirdpage.html')
def hny(request):
    return render(request, 'hny.html')
def interests(request):
    return render(request, 'interests.html')
def educationalRecord(request):
    return render(request, 'educationalRecord.html')
def product(request):
    return render(request, 'product.html')
def shop(request):
    return render(request, 'shop.html')
