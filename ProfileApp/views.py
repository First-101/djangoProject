from django.shortcuts import render,redirect, HttpResponse

# Create your views here.
from ProfileApp.form import ProductForm
from ProfileApp.models import Product


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
def listProduct(request):
    return render(request, 'listProduct.html')
def inputProduct(request):
    return render(request, 'inputProduct.html')

lstOurProduct = []
def listProduct(requset):
    context = {'products':lstOurProduct}
    return render(requset,"listProduct.html",context)
def inputProduct(requset) :
    if requset.method == "POST":
        form = ProductForm(requset.POST)
        if form.is_valid() :
            form = form.cleaned_data
            pdNumber = form.get('pdNumber')
            pdName = form.get('pdName')
            pdPrice = float(form.get('pdPrice'))
            pdProfit = form.get('pdProfit')
            pdAmount = form.get('pdAmount')
            pdVat = form.get('pdVat')
            product= Product(pdNumber,pdName,pdPrice,pdProfit,pdAmount,pdVat)
            lstOurProduct.append(product)
            return redirect('listProduct')

        else:
            form =ProductForm(form)
    else:
        form =ProductForm()
    context = {'form':form,"CHECK":requset.method}
    return render(requset,'inputProduct.html',context)