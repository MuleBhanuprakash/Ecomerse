from django.test import TestCase
from .models import Customer, Product, Order


class CustomerTest(TestCase):
    def test_cust(self):
        cus1 = Customer()
        cus1.name = "bhanu"
        cus1.email = "bhanu@email.com"
        cus1.save()

        self.assertEqual(cus1, Customer.objects.get())


class ProductTest(TestCase):

    def test_product(self):
        prod1 = Product()
        prod1.name = "jeans"
        prod1.price = 35000.50
        prod1.digital = False
        prod1.save()

        self.assertEqual(1, Product.objects.count())


class OrderTest(TestCase):
    def test_order(self):
        ord = Order()
        ord.customer = Customer()
        ord.date_ordered="02/03/2007"
        ord.complete=True

        self.assertEqual(ord,Order.objects.get())

