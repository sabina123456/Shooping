from django.shortcuts import render
from django.shortcuts import redirect
from.models import userinfo

# Create your views here.
from django.http import HttpResponse
from . models import userinfo, product, abouts, Home


def index(request):
    data = Home.objects.all()
    return render(request,'index.html')

def about(request):
    data = abouts.objects.all()
    return render(request,"about.html",{'data':data})

def contact(request):
    return render(request,'contact.html')

def products(request):
    return render(request,'products.html')

def singleproduct(request):
    return render(request, 'single-product.html')



def forget(request):
    return render(request,"forget.html")

def base(request):

    return render(request,"base.html")

def users(request):
    userlist = userinfo.objects.all()
    return render(request, "users.html",{'userlist':userlist})


def signup(request):
    try:
        if request.method == "POST":
            obj = userinfo()
            obj.name = request.POST.get('name')
            obj.username = request.POST.get('username')
            obj.password = request.POST.get('password')
            obj.email = request.POST.get('email')
            obj.phone = request.POST.get('contact')
            obj.utype = request.POST.get('utype')
            obj2=userinfo.objects.values_list('username',flat=True)
            if obj.username in obj2:
                return HttpResponse('Username already exist')
            else:
                obj.save()
            print(obj2)
            print("Saved Successfully")
            return redirect('login')

    except:
        pass
    return render(request,'signup.html')


def login(request):
     if request.method == 'POST':
         x = request.POST.get('username')
         y = request.POST.get('password')
         z = userinfo.objects.get(username=x)
         #print(z.password,z.utype,z.phone)
         print(x,y)
         if y==z.password:
            return redirect('index')
         else:
            return HttpResponse('Invalid Password')
         
     return render(request, 'login.html')


def admin_product(request):
   
    if request.method == 'POST':
        obj = product()
        obj.product_id = request.POST.get('product_id')
        obj.product_name = request.POST.get('product_name')
        obj.category = request.POST.get('productcategory')
        obj.price= request.POST.get('productprice')
        obj.quantity = request.POST.get('productquantity')
        obj.Description = request.POST.get('productDescription')
        obj.image = request.POST.get('productimage')
        obj.warranty = request.POST.get('productwarranty')
        obj.save()
        print("save successfully")
   
    return render(request, 'admin_product.html')





    


