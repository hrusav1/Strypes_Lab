from django.db import models
from datetime import date, timedelta
from django.contrib.auth.models import AbstractUser

#definition of some functions that are to be used in the models(fat models lean views)

def log_purchase(user, purchase_type, item_id, amount, quantity, transaction_id):
    return Purchase.objects.create(
        user=user,
        purchase_type=purchase_type,
        item_id=item_id,
        amount=amount,
        quantity=quantity,
        transaction_id=transaction_id
    )

def purchase_module(user, module, transaction_id):
    purchase = log_purchase(user, 'module', module.id, module.price, 1, transaction_id)
    return UserModule.objects.create(user=user, module=module, purchase=purchase)

def purchase_product(user, product, quantity, transaction_id):
    purchase = log_purchase(user, 'product', product.id, product.price * quantity, quantity, transaction_id)
    return UserProduct.objects.create(user=user, product=product, purchase=purchase, quantity=quantity)

def purchase_subscription(user, amount, transaction_id):
    purchase = log_purchase(user, 'subscription', None, amount, 1, transaction_id)
    user.upgrade_to_premium()
    # Set subscription_end_date based on your subscription policy
    user.subscription_end_date = date.today() + timedelta(days=365)  # Set to one year from today
    user.save()
    return purchase


# Create your models here.
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('standard', 'Standard'),
        ('premium', 'Premium'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='standard')
    subscription_end_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def upgrade_to_premium(self):
        self.user_type = 'premium'
        self.save()

    def downgrade_to_standard(self):
        self.user_type = 'standard'
        self.save()

class Purchase(models.Model):
    PURCHASE_TYPE_CHOICES = (
        ('subscription', 'Subscription'),
        ('module', 'Module'),
        ('product', 'Product'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    purchase_type = models.CharField(max_length=20, choices=PURCHASE_TYPE_CHOICES)
    item_id = models.IntegerField(null=True, blank=True)  # ID of the module or product
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    purchase_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.purchase_type} - {self.purchase_date}"

class Apiary(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='apiaries')


class Hive(models.Model):
    apiary = models.ForeignKey(Apiary, on_delete=models.CASCADE, related_name='hives')
    hive_id = models.CharField(max_length=50)
    queen_age = models.IntegerField()
    last_inspection_date = models.DateField()
    notes = models.TextField(blank=True)


class Inspection(models.Model):
    hive = models.ForeignKey(Hive, on_delete=models.CASCADE, related_name='inspections')
    date = models.DateField()
    brood_pattern = models.CharField(max_length=50)
    queen_seen = models.BooleanField()
    disease_signs = models.TextField(blank=True)
    treatment_applied = models.TextField(blank=True)
    notes = models.TextField(blank=True)


class Module(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    characteristics = models.JSONField(default=dict)  # Store module-specific characteristics


class UserModule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_modules')
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.SET_NULL, null=True, related_name='user_modules')
    is_active = models.BooleanField(default=True)


class SensorData(models.Model):
    hive = models.ForeignKey(Hive, on_delete=models.CASCADE, related_name='sensor_data')
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    # Add other sensor data fields as needed


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    

class UserProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.SET_NULL, null=True, related_name='user_products')
    quantity = models.PositiveIntegerField(default=1)