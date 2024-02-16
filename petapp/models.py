from django.db import models
from django.contrib.auth.models import User

# Create your models here. 
# CASECADE: Delete both side, SET NULL: if delete means it became null, SET DEFAULT: 
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=11,default=99999999)

# meta will give extra options ex db table, ordering:ass or des
    class Meta:  
        db_table='customer'

gender = (('Male', 'Male'), ('Female', 'Female'))
class Pet(models.Model):
    name = models.CharField(max_length=15, null=False)
    photo = models.ImageField(upload_to='images')
    breed = models.CharField(max_length=15, null=True)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=6, choices=gender)
    price = models.FloatField(default=0)
    description = models.CharField(max_length=255,default="Description about pet!")

    class Meta:
        db_table = 'pet'

class CartItems(models.Model):
    pet = models.ForeignKey(Pet, on_delete = models.CASCADE,null=True)
    quantity = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'cart_items'


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    building_name = models.CharField(max_length=50, null=False)
    street = models.CharField(max_length=50, null=False)
    landmark = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=30, null=False)
    state = models.CharField(max_length=30, null=False)
    zipcode = models.CharField(max_length=6, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'address'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    shipping_address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'order'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, related_name='items', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_cost(self):
        return self.price * self.quantity


        