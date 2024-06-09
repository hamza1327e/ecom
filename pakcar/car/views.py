from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from car.models import Contact, Product, Category, Order
from django.contrib import messages
from .forms import OrderForm
from django.utils import timezone
# Create your views here.


def HomePage(request):
    products = Product.get_all_products()
    data={'products':products}
    return render(request, 'home.html',data)
    
    


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("Your password and confirm Password are not same!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect("home")

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return redirect('home')
        else:
            return HttpResponse("Username and pass incorrect!")

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('home')


def ContactPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        messages.success(
            request, "Thank You For Contacting Us, we will get back soon!")
    return render(request, 'contact.html')


def AboutPage(request):
    return render(request, 'about.html')


def ProductPage(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'products.html', data)


def __str__(self):
    return self.name


def submit_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Assuming you have a hidden input field in the form with the product ID
            product_id = request.POST.get('product_id')
            product = Product.objects.get(pk=product_id)
            order = form.save(commit=False)
            order.product = product
            order.save()
    else:
        form = OrderForm()
    return render(request, 'order_page.html', {'form': form})



def order_page(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'order_page.html', {'product': product})

