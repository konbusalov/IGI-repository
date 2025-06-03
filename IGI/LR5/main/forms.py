from django import forms
from django.core.validators import MinValueValidator, RegexValidator
from .models import Customer, Employee, User, Product, Supplier

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={
                'pattern': '.{8,}',
                'title': 'Password must be at least 8 characters'
            }),
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 4:
            raise forms.ValidationError("Username must be at least 4 characters")
        return username

class CustomerForm(forms.ModelForm):
    phone = forms.CharField(validators=[
        RegexValidator(
            regex=r'^\+375 \(\d{2}\) \d{3}-\d{2}-\d{2}$',
            message="Phone must be in format +375 (XX) XXX-XX-XX"
        )
    ])
    age = forms.IntegerField(validators=[MinValueValidator(18)])
    
    class Meta:
        model = Customer
        fields = ['phone', 'age']
        widgets = {
            'phone': forms.TextInput(attrs={
                'pattern': '\+375 \(\d{2}\) \d{3}-\d{2}-\d{2}',
                'title': '+375 (XX) XXX-XX-XX'
            }),
            'age': forms.NumberInput(attrs={
                'min': '18'
            })
        }

class EmployeeForm(forms.ModelForm):
    phone = forms.CharField(validators=[
        RegexValidator(
            regex=r'^\+375 \(\d{2}\) \d{3}-\d{2}-\d{2}$',
            message="Phone must be in format +375 (XX) XXX-XX-XX"
        )
    ])
    age = forms.IntegerField(validators=[MinValueValidator(18)])
    
    class Meta:
        model = Employee
        fields = ['position', 'phone', 'age', 'photo']
        widgets = {
            'phone': forms.TextInput(attrs={
                'pattern': '\+375 \(\d{2}\) \d{3}-\d{2}-\d{2}',
                'title': '+375 (XX) XXX-XX-XX'
            }),
            'age': forms.NumberInput(attrs={
                'min': '18'
            })
        }

class ProductForm(forms.ModelForm):
    price = forms.DecimalField(validators=[MinValueValidator(0.01)])
    quantity = forms.IntegerField(validators=[MinValueValidator(0)])
    
    class Meta:
        model = Product
        fields = ['article', 'name', 'price', 'suppliers', 'category', 'quantity']
        widgets = {
            'price': forms.NumberInput(attrs={
                'min': '0.01',
                'step': '0.01'
            }),
            'quantity': forms.NumberInput(attrs={
                'min': '0'
            })
        }

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'address', 'phone']