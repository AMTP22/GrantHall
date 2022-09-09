from django.test import TestCase
from users.models import Cadet

class ClientTestCase(TestCase):
    def setUp(self):
        Client.objects.create(customerID=1, firstName="John", lastName="Doe", cadet=False, faculty=True, stockPerson=False)
        Client.objects.create(customerID=2, first="Jane", last="Doe", cadet=True, faculty=False, stockPerson=False)
        Client.objects.create(customerID=3, first="Tom", last="Doe", cadet=False, faculty=True, stockPerson=False)
    def test_clients_(self):
        johndoe = Client.objects.get(customerID=1)
        janedoe = Client.objects.get(customerID=2)
        tomdoe = Client.objects.get(customerID=3)
        self.assertEqual(johndoe.firstName(), 'John')
        self.assertEqual(janedoe.firstName(), 'Jane')
        self.assertEqual(tomdoe.firstName(), 'Tom')

class OrderTestCase(TestCase):
    def setUp(self):
        Order.objects.create(orderDate="sample", orderTime="sample", orderID=1, orderType="food", client=1, quantity=1)
        Order.objects.create(orderDate="sample", orderTime="sample", orderID=2, orderType="food", client=2, quantity=1)
        Order.objects.create(orderDate="sample", orderTime="sample", orderID=3, orderType="food", client=3, quantity=1)
    def test_clients_(self):
        o1 = Order.objects.get(orderID=1)
        o2 = Order.objects.get(orderID=2)
        o3 = Order.objects.get(orderID=3)
        self.assertEqual(o1.client(), 1)
        self.assertEqual(o2.client(), 2)
        self.assertEqual(o3.client(), 3)

class OrderItemTestCase(TestCase):
    def setUp(self):
        OrderItem.objects.create(order=1, item="pizza")
        OrderItem.objects.create(order=2, item="banana")
        OrderItem.objects.create(order=3, item="salad")
    def test_clients_(self):
        o1 = OrderItem.objects.get(order=1)
        o2 = OrderItem.objects.get(order=2)
        o3 = OrderItem.objects.get(order=3)
        self.assertEqual(o1.item(), "pizza")
        self.assertEqual(o2.item(), "banana")
        self.assertEqual(o3.item(), "salad")

class ItemTestCase(TestCase):
    def setUp(self):
        Item.objects.create(stockQuantity=5,foodName="pizza",price=5,expirationDate="sample",calories=250,sodium=200,sugar=15,fat=40)
        Item.objects.create(stockQuantity=6,foodName="banana",price=5,expirationDate="sample",calories=250,sodium=200,sugar=15,fat=40)
        Item.objects.create(stockQuantity=7,foodName="salad",price=5,expirationDate="sample",calories=250,sodium=200,sugar=15,fat=40)
    def test_clients_(self):
        i1 = Item.objects.get(foodName="pizza")
        i2 = Item.objects.get(foodName="banana")
        i3 = Item.objects.get(foodName="salad")
        self.assertEqual(i1.stockQuantity(), 5)
        self.assertEqual(i2.stockQuantity(), 6)
        self.assertEqual(i3.stockQuantity(), 7)
