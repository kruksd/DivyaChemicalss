import re
from django.shortcuts import render

from divyaChemicalsWebsite.models import blogPage, contactQuery, divyaProducts, downloadModel



# Create your views here.
def makelist(obj):
    lt = obj.split(";")
    ans = []
    for i in lt:
        i = i.replace('\r\n', "")
        if ':' in i:
            slt = i.split(':')
            ans.append(slt)
        else:
            ans.append(i)
    return ans

def home(request):
    blogs = blogPage.objects.all().filter(blogId__lt=4)
    return render(request, 'index.html',{'blogs':blogs})

def about(request):
    return render(request,'about.html')    

def downloads(request):
    download_query=''
    if request.GET.get('download_query'):
        download_query=request.GET.get('download_query')
    downloads = downloadModel.objects.all().filter(fileName__icontains=download_query)
    return render(request,'downloads.html',{'downloads':downloads})

def contact(request):
    return render(request,'contact.html')

def blogs(request):
    search_query=''
    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')
    blogs = blogPage.objects.all().filter(blogTitle__icontains=search_query)
    return render(request, 'blogs.html', {'blogs': blogs})

def blogView(request, title):
    blogs = blogPage.objects.filter(blogTitle=title)
    rblogs=blogPage.objects.all().filter(blogTitle=title)
    return render(request, 'blog-details.html', {'blogs': blogs,'rblogs':rblogs})

def productss(request,type):
   
    products=divyaProducts.objects.filter(productType=type)
    return render(request,'products.html',{'products':products,'type':type})



def productInfo(request,type):
    products=divyaProducts.objects.filter(productName=type)
    productDetails=makelist(products[0].productPoints)
    return render(request,'product-info.html',{'products':products,'productDetails':productDetails})



def portfolio(request):
   

    return render(request, 'clientel.html')




def querySet(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobilenumber=request.POST.get('subject')
        message=request.POST.get('message')
        book, created = contactQuery.objects.get_or_create(name=name,email=email, mobilenumber=mobilenumber,message=message)
        blogs = blogPage.objects.all().filter(blogId__lt=4)
        return render(request, 'index.html',{'blogs':blogs})