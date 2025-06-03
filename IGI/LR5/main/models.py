from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, RegexValidator

class CompanyInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    legal_details = models.TextField(verbose_name="Legal Details")
        
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/')
    pub_date = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    date_added = models.DateField(auto_now_add=True)
        
    def __str__(self):
        return self.question[:50]
    
class JobOpening(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField()
    salary = models.CharField(max_length=100, blank=True)
        
    def __str__(self):
        return self.title

class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 - Very Poor'),
        (2, '2 - Poor'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Excellent'),
    ]
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review by {self.author.username}"

class PromoCode(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    valid_until = models.DateField()
        
    def __str__(self):
        return f"{self.code} ({self.discount}%)"

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    article = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    suppliers = models.ManyToManyField(Supplier, blank=True, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/', blank=True)

    def __str__(self):
        return f"{self.name} ({self.article})"
    
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')
    position = models.CharField(max_length=100)
    phone = models.CharField(
        max_length=20,
        validators=[RegexValidator(regex=r'^\+375 \(\d{2}\) \d{3}-\d{2}-\d{2}$')],
        unique=True
    )
    photo = models.ImageField(upload_to='employees/', null=True, blank=True)
    age = models.IntegerField(validators=[MinValueValidator(18)])
    responsibilities = models.TextField()
        
    def __str__(self):
        return f"{self.user.get_full_name()} ({self.position})"
    
class Customer(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='customer'
    )
    
    phone_regex = RegexValidator(regex=r'^\+375 \(\d{2}\) \d{3}-\d{2}-\d{2}$')
    phone = models.CharField(max_length=20, validators=[phone_regex])
    age = models.IntegerField(validators=[MinValueValidator(18)])

    def __str__(self):
        return f"{self.user.username}"

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Sale #{self.id}"
    
    @property
    def total_price(self):
        return self.product.price * self.quantity

