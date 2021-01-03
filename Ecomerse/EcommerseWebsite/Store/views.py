from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json


# Create your views here.

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderid_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    products=Product.objects.all()
    context={'products':products,'cartItems':cartItems}
    return render(request,'Store/Store.html',context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderid_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order = {'get_cart_total': 0,'get_cart_items': 0,'shipping': False}
        cartItems = order['get_cart_items']
    context={'items': items, 'order': order,'cartItems': cartItems}
    return render(request,'Store/Cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderid_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0,'shipping': False}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order,'cartItems':cartItems}
    return render(request,'Store/Checkout.html',context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('action:', action)
    print('productIt:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderId, created = OrderId.objects.get_or_create(order=order,product=product)

    if action == 'add':
        orderId.quantity = (OrderId.quantity+1)
    elif action == 'remove':
        orderId.quantity = (OrderId.quantity-1)
    orderId.save()

    if orderId.quantity <= 0:
        orderId.delete()
    return JsonResponse('Item was added!', safe=False)