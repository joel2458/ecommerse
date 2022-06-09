import os
from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from ecommersApp import models

from ecommersApp.models import user_Member,category,Product,product_multimage
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
         
        return render(request,'home.html')


@login_required(login_url='user_login')
def about(request):
    if 'uid' in request.session:
        u_uid=request.session["uid"]
        products=models.Product.objects.all()
        if 'product_ids' in request.COOKIES:
            product_ids = request.COOKIES['product_ids']
            counter=product_ids.split('|')
            product_count_in_cart=len(set(counter))
        else:
            product_count_in_cart=0
        return render(request,'user_product.html',{'products':products,'product_count_in_cart':product_count_in_cart,'u_uid':u_uid})
    return redirect('user_login',)


def load_user_signup(request):
    return render(request,'user_signup.html')
def load_user_login(request):
    return render(request,'user_login.html')


def load_admin_home(request):
    if not request.user.is_staff: 
        return redirect('load_user_login')  
    return render(request,'admin_home.html')
@login_required(login_url='user_login')
def load_user_home(request):
    if 'uid' in request.session:
        return render(request,'user_home.html')
    return redirect('load_user_login')


#@login_required(login_url='login')
#def load_add_category(request):
 #   uid = category.objects.get(id=request.session["uid"])
  #  return render(request,'admin_add_category.html',{'uid':uid})


def load_add_category(request):
    return render(request,'admin_add_category.html')

def load_admin_edit_product(request,pk):
    umember=Product.objects.get(id=pk)
    
    return render(request,'admin_edit_product.html',{'umember':umember} )



def user_signup(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        cemail=request.POST['cemail']
        password=request.POST['password']
        cpass=request.POST['cpass']
        add=request.POST['add']
        gender=request.POST['gender']
        phone=request.POST['phn']
        pin=request.POST['pin']
        if request.FILES.get('file') is not None:
            image=request.FILES['file']
        else:
            image="/static/image/defaultimg.png"
        print("hii")
        if password == cpass:
            if email == cemail:
                if User.objects.filter(username=uname).exists():
                    messages.info(request,"Username is allready exist")
                    return redirect('load_user_signup')
                else:
                    user=User.objects.create_user(
                        first_name=fname,
                        last_name=lname,
                        username=uname,
                        email=email,
                        password=password
                    )
                    user.save()
                    
                    print("save")
                    u=User.objects.get(id=user.id)
                    member=user_Member(user_address=add,user_gender=gender,user_image=image,phone=phone,pincode=pin,user=u)
                    member.save()
                    messages.info(request,"successfully Registered")
                    return redirect('load_user_login')
            else:
                messages.info(request,"Email id not matching!!")
                return redirect('load_user_signup')
        else:
            messages.info(request,"password is not matching!!")
            return redirect('load_user_signup')
           
    else:
        return render(request,'user_signup.html')


def user_login(request): 
    try:
        if request.method == 'POST':
            try:
                username = request.POST['username']
                password = request.POST['password']
              
                user = auth.authenticate(username=username, password=password)
                request.session["uid"] = user.id
                if user is not None:
                    if user.is_staff:
                        auth.login(request,user)
                        return redirect('admin_show_product') 
                    else:                     
                        auth.login(request, user)
                        messages.info(request, f'Welcome {username}')
                        return redirect('homepage')
                else:
                    messages.info(request, "invalid details")
                    return redirect('load_user_login')
            except:
                messages.info(request, "invalid details1")
                return render('user_login.html')
        else:
            messages.info(request, "invalid details2")
            return render('user_login.html')
    except:
        messages.info(request, 'Invalid username or password')
        return render(request, 'user_login.html')

@login_required(login_url='user_login')
def show_profile(request):
   
        user=user_Member.objects.filter(user=request.user)
        return render(request,'user_profile.html',{'user':user })

@login_required(login_url='user_login')
def user_edit_profile(request):
    if request.method == 'POST':
        
      
        umember=user_Member.objects.get(user=request.user)
        umember.user.first_name = request.POST.get('fname')
        umember.user.last_name = request.POST.get('lname')
        umember.user.username = request.POST.get('uname')
        umember.user.email = request.POST.get('email')
        print("helloww")
        umember.user_address = request.POST.get('add')
        umember.user_gender = request.POST.get('gender')
        umember.phone = request.POST.get('phn')
        umember.pincode = request.POST.get('pin')
        print("helloww")
        if request.FILES.get('file') is not None:
            if not umember.user_image == "/static/image/defaultimg.png":
                os.remove(umember.user_image.path)
                umember.user_image = request.FILES['file']
            else:
                umember.user_image = request.FILES['file']
        else:
            os.remove(umember.user_image.path)
            umember.user_image = "/static/image/defaultimg.png"
        
        umember.user.save()
        umember.save()
       
        return redirect('show_profile')
    
    umember=user_Member.objects.get(user=request.user)
        
    return render(request,'user_edit_profile.html',{'umember':umember})


@login_required(login_url='login')
def add_category(request):
    if request.method=='POST':
        cat=request.POST['category']
        
        print(cat)
        crs=category()
        crs.category_name=cat
       
        crs.save()
        print("hii")
        return redirect('admin_show_product')


def logout(request):
    request.session["uid"] = ""
    auth.logout(request)
    return redirect('homepage')


def load_admin_add_product(request):
    catgrs = category.objects.all()
    context={
        'catgrs':catgrs
    }
    return render(request,'admin_add_product.html',context)

def add_product(request):
    if request.method == 'POST':
        catgors = request.POST.get('category')
        cts = category.objects.get(id=catgors)
        name = request.POST.get('name')
        img = request.FILES.get('image')
        price = request.POST.get('price')
        desc = request.POST.get('des')
        prdct = Product(category=cts,name=name,product_image=img,price=price,description=desc)
        prdct.save()
        print("save")
        return redirect('admin_show_product')
    return render(request,'admin_add_product.html')

def load_admin_show_product(request):
    if not request.user.is_staff: 
        return redirect('load_user_login')  
    return render(request,'admin_show_product.html')

def admin_show_product(request):
    ctgs = request.GET.get('category')
    imgs = Product.objects.all()
    if ctgs is not None:
        imgs = Product.objects.filter(category__category_name=ctgs)
    catgrs = category.objects.all()
    
    context = {
        'catgrs':catgrs,
        'imgs':imgs,
        }
    return render(request,'admin_show_product.html',context)

def admin_edit_product(request,pk):
    if request.method == 'POST':
        umember=Product.objects.get(id=pk)
        umember.name = request.POST.get('name')
        umember.price = request.POST.get('price')
        umember.discription = request.POST.get('des')
        
        if request.FILES.get('file') is not None:
            if not umember.product_image == "/static/image/defaultimg.png":
                os.remove(umember.product_image.path)
                umember.product_image = request.FILES['file']
            else:
                umember.product_image = request.FILES['file']
        else:
            os.remove(umember.product_image.path)
            umember.product_image = "/static/image/defaultimg.png"
        
        umember.save()
        return redirect('admin_show_product')


def admin_delete_product(request,pk):
    udelete=Product.objects.get(id=pk)
    if udelete.product_image is not None:
        if not udelete.product_image == "/static/image/defaultimg.png":
            os.remove(udelete.product_image.path)
        else:
            pass
    udelete.delete()
    return redirect('admin_show_product')

def user_show_product(request):
    ctgs = request.GET.get('category')
    uimg = Product.objects.all()
    if ctgs is not None:
        uimg = Product.objects.filter(category__category_name=ctgs)
    ucatgrs = category.objects.all()
    
    context = {
        'ucatgrs':ucatgrs,
        'uimg':uimg,
        }
    return render(request,'user_product.html',context)

def load_mul(request):
   
    cti = Product.objects.all()
    return render(request,'admin_add_mulimage.html',{'cti':cti})
    


def add_mul_img(request):
    if request.method == 'POST':
        nme= request.POST.get('name')
        cti = Product.objects.get(id=nme)
        img = request.FILES.getlist('images')
        for i in img:
            prdcts= product_multimage(product=cti,multimage=i)
            
            prdcts.save()
            print("save")
        return redirect('admin_show_product')
    return render(request,'admin_add_mulimage.html')

    

def showimage(request,pk):
    img = Product.objects.get(id=pk)
    mulimgs = product_multimage.objects.filter(product_id=img.id)
    # linkimg = product_multimage.objects.get(id=pk)
    context={
        'img':img,
        'mulimgs':mulimgs,
        # 'linkimg':linkimg,
    }
    return render(request,'admin_product_details.html',context)



@login_required(login_url='user_login')
def add_to_cart_view(request,pk):
    if 'uid' in request.session:
        u_uid=request.session["uid"]
        products=models.Product.objects.all()
        #for cart counter, fetching products ids added by customer from cookies
        if 'product_ids' in request.COOKIES:
            product_ids = request.COOKIES['product_ids']
            counter=product_ids.split('|')
            product_count_in_cart=len(set(counter))
        else:
            product_count_in_cart=1
        response = render(request, 'about.html',{'products':products,'product_count_in_cart':product_count_in_cart,'u_uid':u_uid})
        #adding product id to cookies
        if 'product_ids' in request.COOKIES:
            product_ids = request.COOKIES['product_ids']
            if product_ids=="":
                product_ids=str(pk)
            else:
                product_ids=product_ids+"|"+str(pk)
            response.set_cookie('product_ids', product_ids)
        else:
            response.set_cookie('product_ids', pk)
        product=models.Product.objects.get(id=pk)
        messages.info(request, product.name + ' added to cart successfully!')
        return response
    return redirect('user_login')



# for checkout of cart
@login_required(login_url='user_login')
def cart_view(request):
    if 'uid' in request.session:
        current_id = request.user.id
        u_uid=request.session["uid"]
        #for cart counter
        if 'product_ids' in request.COOKIES:
            product_ids = request.COOKIES['product_ids']
            counter=product_ids.split('|')
            product_count_in_cart=len(set(counter))
        else:
            product_count_in_cart=0

        # fetching product details from db whose id is present in cookie
        products=None
        total=0
        if 'product_ids' in request.COOKIES:
            product_ids = request.COOKIES['product_ids']
            if product_ids != "":
                product_id_in_cart=product_ids.split('|')
                products=models.Product.objects.all().filter(id__in = product_id_in_cart)

                #for total price shown in cart
                for p in products:
                    total=total+p.price
        return render(request,'cart.html',{'products':products,'total':total,'product_count_in_cart':product_count_in_cart,'u_uid':u_uid})
    return redirect('user_login')

@login_required(login_url='user_login')
def remove_from_cart_view(request,pk):
    if 'uid' in request.session:
        u_uid=request.session["uid"]
        #for counter in cart
        if 'product_ids' in request.COOKIES:
            product_ids = request.COOKIES['product_ids']
            counter=product_ids.split('|')
            product_count_in_cart=len(set(counter))
        else:
            product_count_in_cart=0

        # removing product id from cookie
        total=0
        if 'product_ids' in request.COOKIES:
            product_ids = request.COOKIES['product_ids']
            product_id_in_cart=product_ids.split('|')
            product_id_in_cart=list(set(product_id_in_cart))
            product_id_in_cart.remove(str(pk))
            products=models.Product.objects.all().filter(id__in = product_id_in_cart)
            #for total price shown in cart after removing product
            for p in products:
                total=total+p.price

            #  for update coookie value after removing product id in cart
            value=""
            for i in range(len(product_id_in_cart)):
                if i==0:
                    value=value+product_id_in_cart[0]
                else:
                    value=value+"|"+product_id_in_cart[i]
            response = render(request, 'cart.html',{'products':products,'total':total,'product_count_in_cart':product_count_in_cart,'u_uid':u_uid})
            if value=="":
                response.delete_cookie('product_ids')
            response.set_cookie('product_ids',value)
            return response
    return redirect('user_login')


@login_required(login_url='user_login')
def detail(request,pk):
    if 'uid' in request.session:
        products=Product.objects.filter(id=pk)
        product=Product.objects.get(id=pk)
        mulimgs = product_multimage.objects.filter(product_id=product.id)
        # related=models.Product.objects.filter(category_id=products.category_id).exclude(id=pk)
        related=Product.objects.filter(category_id=product.category_id).exclude(id=pk)
        context={'products':products,'related':related,'product':product,'mulimgs':mulimgs}
        return render(request,"view_product.html",context,)
    return redirect('user_login')


@login_required(login_url='user_login')
def show_user_details(request):
    user=user_Member.objects.all()
    context={'user':user}
    return render(request,'admin_show_user.html',context)

@login_required(login_url='loginpage')
def delete_user(request,pk):
    udelete=user_Member.objects.get(id=pk)
    if udelete.user_image is not None:
        if not udelete.user_image == "/static/image/defaultimg.png":
            os.remove(udelete.user_image.path)
        else:
            pass
    udelete.delete()
    return redirect('show_user_details')







