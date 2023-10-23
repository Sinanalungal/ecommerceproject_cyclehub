from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'index.html')
def shop(request):
    return render(request,'product.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def admin_panel(request):
    return render(request,'admin_panel.html')
def cart(request):
    return render(request,'cart.html')
def checkout(request):
    return render(request,'checkout.html')
def wishlist(request):
    return render(request,'wishlist.html')
def detail(request):
    return render(request,'detail.html')
def admin_products(request):
    return render(request,'admin_products.html')
def admin_order(request):
    return render(request,'admin_order.html')
def add_products(request):
    return render(request,'add_products.html')
def edit_products(request):
    return render(request,'edit_products.html')
def admin_users(request):
    return render(request,'admin_users.html')
def admin_categories(request):
    return render(request,'admin_categories.html')
def add_categories(request):
    return render(request,'add_categories.html')
def edit_categories(request):
    return render(request,'edit_categories.html')
def admin_brands(request):
    return render(request,'admin_brands.html')
def add_brands(request):
    return render(request,'add_brands.html')
def edit_brands(request):
    return render(request,'edit_brands.html')
def admin_coupons(request):
    return render(request,'admin_coupons.html')
def add_coupons(request):
    return render(request,'add_coupons.html')
def admin_banners(request):
    return render(request,'admin_banners.html')
def add_banners(request):
    return render(request,'add_banners.html')
def admin_payments(request):
    return render(request,'admin_payment.html')