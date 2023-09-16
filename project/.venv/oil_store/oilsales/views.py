from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Product, Order, OrderItem
from .forms import RegistrationForm
from django.shortcuts import get_object_or_404
from django.contrib import messages  # Import the messages module


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})

def home(request):
    products = Product.objects.all()
    return render(request, 'oilsales/home.html', {'products': products})

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    order, created = Order.objects.get_or_create(customer=request.user)
    OrderItem.objects.create(order=order, product=product, quantity=1)
    return redirect('home')

@login_required
def view_cart(request):
    order = Order.objects.get(customer=request.user)

    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item = get_object_or_404(OrderItem, id=item_id)
        if item.order == order:
            item.delete()
    
    total_price = sum(item.product.price * item.quantity for item in order.orderitem_set.all())
    
    return render(request, 'oilsales/cart.html', {'order': order, 'total_price': total_price})


# ... (other views)

@login_required
def place_order(request):
    if request.method == 'POST':
        order = Order.objects.get(customer=request.user)
        order.address = request.POST['address']
        order.total_price = sum(item.product.price * item.quantity for item in order.orderitem_set.all())
        order.save()

        # Add a success message
        messages.success(request, 'Your order has been placed successfully!')

        # Clear the cart (delete all items associated with the order)
        order.orderitem_set.all().delete()

        # Redirect to the cart page with a message
        return redirect('view_cart')
    else:
        return render(request, 'oilsales/place_order.html')
