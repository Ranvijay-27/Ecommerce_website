from cmath import log
from django.shortcuts import render

# Create your views here.
from cgitb import html
from itertools import product
from multiprocessing import context
from tkinter import Button
from tkinter.tix import STATUS
from django.http import JsonResponse
from django.shortcuts import redirect, render
from.models import *
from django.contrib import messages
from .forms import CustomUserForm
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail,EmailMultiAlternatives
from review_project.settings import EMAIL_HOST_USER
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from review_app.forms import ReviewAdd


# Create your views here.
def index(request):
   
    product  = Product.objects.filter(trending = 1)
    cart = ProductReview.objects.filter(review_rating = 1)
    
    # return render(request,'view.html',con)
    return render(request,'index.html',{'products':product,'cart':cart})
def main(request):
    return render(request,'main.html')
def colections(request):
    category = Category.objects.filter(status=0)
    context = {'category':category}
    return render(request,'colections.html',context)
def colectionsview(request,slug):
    
    if(Category.objects.filter(slug = slug,status = 0)):
        product = Product.objects.filter(category__slug = slug)
        category = Category.objects.filter(slug = slug).first()
        context = {'product':product,'category': category}
        return render(request,'index1.html',context)
    else:
        messages.warning(request, "No such category found")
        return redirect("colections")
    # return render(request,'colectionsview')  
def showreview(request):
    if request.method == 'POST':
        p_id = request.POST.get('p_id')
        cart = ProductReview.objects.filter(product=p_id)
        return render(request ,'view.html',{'cart':cart})
    return render(request,'view.html')
    
      
def productview(request,cate_slug,prod_slug):
    # p_id = request.POST.get('p_id')
    # cart = ProductReview.objects.filter(product=p_id)
    cart = ProductReview.objects.filter(name = prod_slug)
    # return render(request,'view.html',{'cart':cart})    
    
        
    if(Category.objects.filter(slug = cate_slug,status = 0)): 
        if(Product.objects.filter(slug = cate_slug,status = 0)):
            product = Product.objects.filter(slug = prod_slug,status=0).first()
            # context = {'product':product}
            
        else:
            messages.error(request,"No such product Found")
            return redirect('colections')    
    else:
        messages.error(request,"No such category Found")
        return redirect('colections')
    return render(request,'view.html',{'product':product,'cart':cart})
    # return render(request,'view.html')

def register(request):
    form = CustomUserForm()
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Register Successfully Login to Continue")
            return render(request,'login.html')
    context = {'form':form}
    return render(request,'register.html',context)
def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,"You are Alredy login")
        return redirect('/')
    else:    
        if request.method == 'POST':
            name = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username = name,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid Username or Password")
                return render(request,"login.html") 
    return render(request,'login.html')

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logout Out Successfully")
    return redirect('/')
def addtocart(request):
    if request.method  == 'POST' :
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id')) 
            product_check = Product.objects.get(id = prod_id)
            if (product_check):
                if(Cart.objects.filter(user = request.user.id,product_id = prod_id)):
                    prod_qty = int(request.POST.get('product_qty'))
                    cart = Cart.objects.get(product_id=prod_id,user=request.user)
                    cart.product_qty = prod_qty
                    cart.save()
                    return JsonResponse({'status':"Item Updated In Cart"})
              
                else :
                    prod_qty = int(request.POST.get('product_qty'))  
                    if product_check.quantity >= prod_qty:
                        Cart.objects.create(user=request.user,product_id = prod_id ,product_qty= prod_qty) 
                        messages.success(request,"Product added successfully")
                        return JsonResponse({'status':"Product added successfully"})
                    else:
                        return JsonResponse({'status':"Only"+ str(product_check.quantity) + "quantity available"})   
            else:
                return JsonResponse({'status':"No Such Product Found"})
        else:
            return JsonResponse({'status':"Login to continue"})         
    return redirect('/')
    
            
  
    # return render (request,'cart.html')


# def checkout(request):
#     rawcart  = Cart.objects.filter(user = request.user)
#     for item in rawcart:
#         if item.product_qty > item.product.quantity:
#             Cart.objects.delete(id= item.id)
#     cartitem = Cart.objects.filter(user=request.user,)
#     total_price = 0
#     for item in cartitem:
#         if item.product.price >= 10000:
#             messages.success(request,"You Can Not")
            
#         else:
#             total_price = total_price + item.product.price * item.product_qty
#             context={'cartitem': cartitem, 'total_price':total_price} 
#             messages.success(request,"You Can Not Buy Item Less Than 10,000")   
#             return render(request,'checkout.html' ,context)
#     return render(request,'checkout.html')
# if request.method == 'POST':
#             p_id = request.POST.get('p_id')
#             cart = ProductReview.objects.filter(product = 7)
#             con = {'cart':cart}
#             return render(request,'view.html',con)



def checkout(request):
    rawcart  = Cart.objects.filter(user = request.user)
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            # Cart.objects.delete(id= item.id)
            cartitem = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cartitem:
        total_price = total_price + item.product.price * item.product_qty
    context={'cartitem': cartitem, 'total_price':total_price}    
    return render(request,'checkout.html' ,context)

# @login_required(login_url='loginpage')   
def cart(request):
   
    cart = Cart.objects.filter(user = request.user)
     
    rawcart  = Cart.objects.filter(user = request.user)
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            Cart.objects.get(id= item.id)
    cartitem = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cartitem:
        total_price = total_price + item.product.price * item.product_qty
        context1={'cartitem': cartitem, 'total_price':total_price} 
    context = {'cart':cart,'total_price':total_price}    
    if request.method=='POST':
        price1 = int(request.POST.get('price1'))
        if price1 <= 10000:
            return render(request,'checkout.html',context1,)
        else:
            messages.success(request,'You Can Not Buy Product Less Than 10,000')
            return render(request,'cart.html',context )
    # Product.objects.update(quantity = item.product.quantity - item.product_qty)
            
    return render(request, 'cart.html',context)

def details(request):
    return render(request, 'details.html')  
def razorpaycheck(request):
    cart = Cart.objects.filter(user = request.user)
    total_price = 0
    for item in cart:
        total_price = total_price + item.product.price * item.product_qty
    return JsonResponse({
        'total_price':total_price
    })    
def success1(request):
    return render(request, 'success1.html') 

# def mails(request):
#     if request.method=="POST":
#         name = request.POST.get('username')
#         password = request.POST.get('email')
#         subject = "Registration Page"
#         from_email = 'ranvijaywhitenetgroup@gmail.com'
#         to = 'ranvijaymaurya.rk@gmail.com'
#         msg = EmailMultiAlternatives(name,password,subject, from_email,[to])
#         msg.content_subtype = 'html'
#         msg.save()
#     #     send_mail(
#     #     'Subject here',
#     #     'Here is the message.',
#     #     'ranvijaywhitenetgroup@gmail.com',
#     #     ['ranvijaymaurya.rk@gmail.com'],
#     #     fail_silently=False,
#     # )
#     return render(request, 'mails.html')



def mails(request):
    if request.method=='POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        msg = '<p>Click Here To Go Registration Page <b>http://localhost:8000/register</b></p>'
        data = "User Name = " + name + " Email = " + email + msg
        
        p1 = EmailMultiAlternatives("get Registration Link",data,EMAIL_HOST_USER,[email])
        p1.content_subtype = "html"
        p1.send()
        # return HttpResponse('hello')
        # return JsonResponse({'status':"No Such Product Found"})
        messages.success(request,"Email Sent Successfully")
        messages.success(request,"check Your Mail")
        # msg = EmailMultiAlternatives( name,email, EMAIL_HOST_USER, ['ranvijaymaurya.rk@gmail.com']  )
        # msg.attach_alternative(html,'text/html')
        # msg.send()
        # send_mail(
        # 'Registration',
        # data,
        # 'ranvijaywhitenetgroup@gmail.com',
        # [email],
        # fail_silently=False,
# )
    return render(request, 'mails.html')   


def productlistAjax(request):
    products = Product.objects.filter(status = 0).values_list('name',flat=True)
    productslist = list(products)
    return JsonResponse(productslist,safe=False)
    
def searchproduct(request):
    if request.method == "POST":
        searchproduct = request.POST.get('productsearch')
        if searchproduct == "":
            return redirect(request.META.get('HTTP_REFERER')) 
        else:
            product = Product.objects.filter(color__contains = searchproduct).first()
            # product = Product.objects.filter(color__contains = searchproduct).first()
            if product:
                return redirect('colections/'+ product.category.slug+'/'+ product.slug)
            else:
                messages.info(request, "No Product Match")
                return redirect(request.META.get('HTTP_REFERER')) 
                        
            
    return redirect(request.META.get('HTTP_REFERER'))    

def productpriceAjax(request):
    products = Product.objects.filter(status = 0).values_list('price',flat=True)
    productslist = list(products)
    return JsonResponse(productslist,safe=False)


def save_review(request):
    if request.method == "POST":
        textreview = request.POST.get('reviewtext')
        reviewrating = request.POST.get('rating')
        product_id = int(request.POST.get('prod_id'))
        name = request.POST.get('prod_name')
        user = request.user
        ProductReview.objects.create(
            user = user,
            product= product_id,
            review_text = textreview,
            review_rating = reviewrating,
            name = name
            ).save()
        messages.success(request,"Thanks For Review This Product!!!!")
    return render(request,'colections.html')



def savereview(request):
    if request.method == "POST":
        product_id = int(request.POST.get('product_id'))
        if(ProductReview.objects.filter(user=request.user,product=product_id)):
            textreview = request.POST.get('product_text')
            reviewrating = request.POST.get('product_rating')
            name = request.POST.get('product_name')
            user = request.user
            cart = ProductReview.objects.get(product=product_id,user_id=request.user)
            cart.user_id = user
            cart.review_text = textreview
            cart.review_rating = reviewrating
            cart.name = name
            cart.save()
            return JsonResponse({'status':"Thanks For Updated This Review!!!!"})
        else:
            ProductReview.objects.create(
            user = user,
            product= product_id,
            review_text = textreview,
            review_rating = reviewrating,
            name = name
            ).save()
        messages.success(request,"Thanks For Review This Product!!!!")
        
        
    return redirect('/')
    
    

def popup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        PopUp.objects.create(
           
            email = email,
            phone = phone
        ).save()
        messages.success(request,"Thanks For Register Shop Here!!!!")
        # return JsonResponse('colections.html', {'status':"Login to continue"})
        return render(request,'colections.html')
    return render(request,'popup.html')

@login_required(login_url='loginpage')
def wishlist(request):
    wishlist = Wichlist.objects.filter(user=request.user)
    context = {'wishlist':wishlist}
    return render(request,'wishlist.html',context)

def addtowishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id = prod_id)
            if(product_check):
                if(Wichlist.objects.filter(user = request.user,product_id = prod_id)):
                    return JsonResponse({'status':"Product Already In Wishlist"}) 
                else:
                    Wichlist.objects.create(user = request.user,product_id = prod_id)
                    return JsonResponse({'status':"Product Added to Wishlist"}) 
                    
            else:
                return JsonResponse({'status':"No Such Product Found"})  
        else:
            return JsonResponse({'status':"Login to continue"})    
        
    return redirect('/')
    
# def update(request,contact_id):
#     if request.method == "POST":
#         textreview = request.POST.get('reviewtext')
#         reviewrating = request.POST.get('rating')
#         product_id = int(request.POST.get('prod_id'))
#         user = request.user
#         contact = ProductReview.objects.get(product=contact_id)
#         form = ReviewAdd(request.POST or None, instance = contact)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'status':"Review Updated"})     
#         else:
#             ProductReview.objects.create(
#                 user = user,
#                 product= product_id,
#                 review_text = textreview,
#                 review_rating = reviewrating
#             ).save()
#             return JsonResponse({'status':"Review Updated"})
#     return render(request,'colections.html')

def updatecart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user,product_id=prod_id)):
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(product_id=prod_id,user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status':"Updated Sucessfully"})
    return redirect('/')

def updateproduct(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Product.objects.filter(id=prod_id)):
            prod_qty = int(request.POST.get('product_qty'))
            cart1 = Product.objects.get(id=prod_id)
            cart1.quantity = cart1.quantity - prod_qty
            cart1.save()
            return JsonResponse({'status':" product in cart Updated Sucessfully"}) 
    return redirect('/')

def deletecartitem(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user,product_id=prod_id)):
            cartitem = Cart.objects.get(product_id=prod_id,user=request.user)
            cartitem.delete()
            return JsonResponse({'status':"Deleted Sucessfully"})
    return redirect('/')

def pricecheck(request):
    if request.method=='POST':
        price1 = int(request.POST.get('price1'))
        if price1 <=10000:
            return render(request,'checkout.html')
        else:
            messages.success(request,'Not go')
    return redirect(request.META.get('HTTP_REFERER'))
            
    # return redirect('/')        
    # return render(request,'cart.html')