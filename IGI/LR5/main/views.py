from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.utils import timezone
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserForm, CustomerForm, EmployeeForm, ProductForm, SupplierForm
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import statistics
from django.db.models import Count, Sum, Avg, F, Q
from django.utils import timezone
import calendar as cal
from django.utils import timezone
import pytz
from decimal import Decimal, getcontext
import requests
import logging
from django.http import JsonResponse

logger = logging.getLogger(__name__)

class HomeView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.path.startswith('/api/'):
            logger.warning(f"Неавторизованный API доступ: {request.path}")
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        # Log that the home view was accessed
        logger.info("HomeView accessed - IP: %s, User: %s", 
                   request.META.get('REMOTE_ADDR'),
                   request.user.username if request.user.is_authenticated else 'Anonymous')
        
        try:
            # Get latest article
            latest_article = Article.objects.order_by('-pub_date').first()
            logger.debug("Latest article: %s", latest_article.title if latest_article else 'No articles found')
            
            # Timezone handling
            tzname = request.COOKIES.get('django_timezone')
            logger.debug("Timezone from cookie: %s", tzname)
            
            try:
                user_tz = pytz.timezone(tzname)
                logger.debug("Timezone set to: %s", tzname)
            except pytz.UnknownTimeZoneError:
                user_tz = pytz.UTC
                logger.warning("Unknown timezone '%s', defaulting to UTC", tzname)
            
            current_time = timezone.now().astimezone(user_tz)
            logger.debug("Current time: %s", current_time)
            
            # Calendar setup
            cal_obj = cal.Calendar()
            month_calendar = cal_obj.monthdayscalendar(current_time.year, current_time.month)
            logger.debug("Calendar generated for %s-%s", current_time.year, current_time.month)
            
            # Cat fact API
            cat_data = None
            try:
                cat_response = requests.get('https://catfact.ninja/fact', timeout=3)
                if cat_response.status_code == 200:
                    cat_data = cat_response.json()
                    logger.debug("Cat fact received: %s", cat_data.get('fact', 'No fact available'))
                else:
                    logger.warning("Cat fact API returned status code: %s", cat_response.status_code)
            except requests.RequestException as e:
                logger.error("Failed to fetch cat fact: %s", str(e), exc_info=True)
            
            # Joke API
            joke_data = None
            try:
                joke_response = requests.get('https://official-joke-api.appspot.com/random_joke', timeout=3)
                if joke_response.status_code == 200:
                    joke_data = joke_response.json()
                    logger.debug("Joke received - Setup: %s", joke_data.get('setup', 'No setup available'))
                else:
                    logger.warning("Joke API returned status code: %s", joke_response.status_code)
            except requests.RequestException as e:
                logger.error("Failed to fetch joke: %s", str(e), exc_info=True)
            
            # Prepare context
            context = {
                'latest_article': latest_article,
                'timezone': tzname,
                'current_day': current_time.day,
                'calendar': month_calendar,
                'current_time': current_time,
                'cat_fact': cat_data.get('fact') if cat_data else None,
                'joke_setup': joke_data.get('setup') if joke_data else None,
                'joke_type': joke_data.get('type') if joke_data else None,
                'joke_punchline': joke_data.get('punchline') if joke_data else None
            }
            
            logger.info("HomeView rendered successfully")
            return render(request, 'main/home.html', context)
            
        except Exception as e:
            logger.critical("Unexpected error in HomeView: %s", str(e), exc_info=True)
            raise  # Re-raise the exception after logging it
    
class AboutView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.path.startswith('/api/'):
            logger.warning(f"Неавторизованный API доступ: {request.path}")
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        logger.info("About page viewed")
        return render(request, 'main/about.html')
    
class NewsView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.path.startswith('/api/'):
            logger.warning(f"Неавторизованный API доступ: {request.path}")
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        articles = Article.objects.all().order_by('-pub_date')
        logger.info(f"News page viewed - {articles.count()} articles loaded")
        return render(request, 'main/news.html', {'articles': articles})

class FAQView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.path.startswith('/api/'):
            logger.warning(f"Неавторизованный API доступ: {request.path}")
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        faqs = FAQ.objects.all()
        logger.info(f"FAQ page viewed - {faqs.count()} FAQs loaded")
        return render(request, 'main/faq.html', {'faqs': faqs})

class ContactView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.path.startswith('/api/'):
            logger.warning(f"Неавторизованный API доступ: {request.path}")
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        employees = Employee.objects.all()
        logger.info(f"Contact page viewed - {employees.count()} employees listed")
        return render(request, 'main/contact.html', {'employees': employees})

class PrivacyPolicyView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.path.startswith('/api/'):
            logger.warning(f"Неавторизованный API доступ: {request.path}")
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        logger.info("Privacy policy viewed")
        return render(request, 'main/privacy_policy.html')

class JobsView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.path.startswith('/api/'):
            logger.warning(f"Неавторизованный API доступ: {request.path}")
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        vacancies = JobOpening.objects.all()
        logger.info(f"Jobs page viewed - {vacancies.count()} vacancies listed")
        return render(request, 'main/jobs.html', {'vacancies': vacancies})

class ReviewsView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.path.startswith('/api/'):
            logger.warning(f"Неавторизованный API доступ: {request.path}")
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        reviews = Review.objects.all()
        logger.info(f"Reviews page viewed - {reviews.count()} reviews loaded")
        return render(request, 'main/reviews.html', {"reviews": reviews})
    
    def post(self, request):
        try:
            review = Review.objects.create(
                author=request.user,
                rating=request.POST.get('rating'),
                text=request.POST.get('text')
            )
            logger.info(f"New review created by {request.user.username} (Rating: {review.rating})")
            return redirect('reviews')
        except Exception as e:
            logger.error(f"Failed to create review: {str(e)}")
            raise

class PromotionsView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.path.startswith('/api/'):
            logger.warning(f"Неавторизованный API доступ: {request.path}")
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        today = timezone.now().date()
        active_promos = PromoCode.objects.filter(
            is_active=True,
            valid_until__gte=today
        )
        archived_promos = PromoCode.objects.exclude(
            is_active=True,
            valid_until__gte=today
        )
        logger.info(
            f"Promotions viewed - Active: {active_promos.count()}, "
            f"Archived: {archived_promos.count()}"
        )
        return render(request, 'main/promocodes.html', {
            'active_promos': active_promos,
            'archived_promos': archived_promos
        })

class ProductsView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.path.startswith('/api/'):
            logger.warning(f"Неавторизованный API доступ: {request.path}")
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        logger.info("Products page accessed")
        
        categories = Category.objects.all()
        products = Product.objects.all()
        logger.debug(f"Loaded {categories.count()} categories and {products.count()} products")

        # Category filter
        category_id = request.GET.get('category')
        if category_id:
            category_id = int(category_id)
            products = products.filter(category_id=category_id)
            logger.debug(f"Filtered by category ID: {category_id}")

        # Price filters
        min_price = request.GET.get('min_price')
        if min_price:
            min_price = float(min_price)
            products = products.filter(price__gte=min_price)
            logger.debug(f"Applied min price filter: {min_price}")

        max_price = request.GET.get('max_price')
        if max_price:
            max_price = float(max_price)
            products = products.filter(price__lte=max_price)
            logger.debug(f"Applied max price filter: {max_price}")

        # Search
        search_query = request.GET.get('search')
        if search_query:
            products = products.filter(
                Q(name__icontains=search_query) | 
                Q(article__icontains=search_query)
            )
            logger.debug(f"Search query: {search_query}")

        # Sorting
        sort = request.GET.get('sort')
        if sort == 'price_asc':
            products = products.order_by('price')
            logger.debug("Sorted by price ascending")
        elif sort == 'price_desc':
            products = products.order_by('-price')
            logger.debug("Sorted by price descending")

        logger.info(f"Returning {products.count()} filtered products")
        return render(request, 'main/products.html', {
            'categories': categories,
            'products': products,
            'selected_category': category_id,
            'min_price': min_price,
            'max_price': max_price,
            'search_query': search_query,
            'sort': sort
        })

class LoginView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.path.startswith('/api/'):
            logger.warning(f"Неавторизованный API доступ: {request.path}")
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        logger.info("Login page accessed")
        return render(request, 'main/login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        logger.info(f"Login attempt for username: {username}")

        user = authenticate(request, username=username, password=request.POST.get('password'))

        if user is not None:
            login(request, user)
            logger.info(f"Successful login for user: {username}")
            return redirect('home')
        else:
            logger.warning(f"Failed login attempt for username: {username}")
            messages.error(request, 'Invalid username or password.')
            return render(request, 'main/login.html')

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        username = request.user.username
        logout(request)
        logger.info(f"User logged out: {username}")
        return redirect("home")
    
class RegisterAsCustomerView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.path.startswith('/api/'):
            logger.warning(f"Неавторизованный API доступ: {request.path}")
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        logger.info("Customer registration page accessed")
        return render(request, 'main/register.html', {
            'user_form': UserForm(),
            'customer_form': CustomerForm()
        })
    
    def post(self, request):
        user_form = UserForm(request.POST)
        customer_form = CustomerForm(request.POST)
        
        if user_form.is_valid() and customer_form.is_valid():
            username = user_form.cleaned_data['username']
            logger.info(f"Customer registration attempt for username: {username}")
            
            if User.objects.filter(username=username).exists():
                logger.warning(f"Username already exists: {username}")
                return render(request, 'main/register.html', {
                    'user_form': user_form,
                    'customer_form': customer_form,
                    'error': 'Username already exists'
                })
            
            user = User.objects.create_user(
                username=username,
                password=user_form.cleaned_data['password']
            )
            
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()
            
            login(request, user)
            logger.info(f"New customer registered: {username}")
            return redirect('home')
            
        logger.warning("Invalid customer registration form submission")
        return render(request, 'main/register.html', {
            'user_form': user_form,
            'customer_form': customer_form
        })

class RegisterAsEmployeeView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.path.startswith('/api/'):
            logger.warning(f"Неавторизованный API доступ: {request.path}")
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        logger.info("Employee registration page accessed")
        return render(request, 'main/register_as_employee.html', {
            'user_form': UserForm(),
            'employee_form': EmployeeForm()
        })       
    
    def post(self, request):
        user_form = UserForm(request.POST, request.FILES)
        employee_form = EmployeeForm(request.POST)
        
        if user_form.is_valid() and employee_form.is_valid():
            username = user_form.cleaned_data['username']
            logger.info(f"Employee registration attempt for username: {username}")
            
            if User.objects.filter(username=username).exists():
                logger.warning(f"Username already exists: {username}")
                return render(request, 'main/register_as_employee.html', {
                    'user_form': user_form,
                    'employee_form': employee_form,
                    'error': 'Username already exists'
                })
            
            user = User.objects.create_user(
                username=username,
                password=user_form.cleaned_data['password']
            )
            
            employee = employee_form.save(commit=False)
            employee.user = user
            employee.save()
            
            login(request, user)
            logger.info(f"New employee registered: {username}")
            return redirect('home')
            
        logger.warning("Invalid employee registration form submission")
        return render(request, 'main/register_as_employee.html', {
            'user_form': user_form,
            'employee_form': employee_form
        })
    

class DashboardView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.path.startswith('/api/'):
            logger.warning(f"Неавторизованный API доступ: {request.path}")
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        user = request.user
        logger.info("Dashboard view - User: %s", user.username)

        if user.is_superuser:
            return render(request, 'main/superuser_dashboard.html', {
                'sales': Sale.objects.all().order_by('-date')[:10],
                'suppliers': Supplier.objects.all(),
                'products': Product.objects.all()
            })
        elif hasattr(user, "employee"):
            return render(request, 'main/employee_dashboard.html', {
                'sales': Sale.objects.all().order_by('-date'),
                'suppliers': Supplier.objects.all()
            })
        elif hasattr(user, "customer"):
            return render(request, 'main/customer_dashboard.html', {
                'products': Product.objects.all(),
                'purchases': Sale.objects.filter(customer=user.customer).order_by("-date")[:5],
                'promos': PromoCode.objects.all()
            })
        else:
            logger.warning("Unauthorized access attempt by: %s", user.username)
            return HttpResponse("You do not have access to this page")
        
class PurchaseProductView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.path.startswith('/api/'):
            logger.warning(f"Неавторизованный API доступ: {request.path}")
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, id):
        user = request.user
        if hasattr(user, "customer"):
            product = Product.objects.get(id=id)
            quantity = int(request.POST.get('quantity'))
            logger.info(f"Customer {user.username} purchased {quantity} of {product.name}")
            sale = Sale.objects.create(product=product, customer=request.user.customer, quantity=quantity)
            sale.save()
            product.quantity -= quantity
            product.save()
            return redirect('dashboard')
        elif hasattr(user, "employee"):
            product = Product.objects.get(id=id)
            quantity = int(request.POST.get('quantity'))   
            logger.info(f"Employee {user.username} restocked {quantity} of {product.name}") 
            product.quantity += quantity
            product.save()
            return redirect('dashboard')
        else:
            return HttpResponse("You dont have permission to do this")
        
class DeleteSupplierView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.path.startswith('/api/'):
            logger.warning(f"Неавторизованный API доступ: {request.path}")
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id):
        supplier = Supplier.objects.get(id=id)
        supplier.delete()
        logger.info(f"User {request.user.username} deleted supplier {supplier.name}")
        return redirect('dashboard')
    
class DeleteProductView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.path.startswith('/api/'):
            logger.warning(f"Неавторизованный API доступ: {request.path}")
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id):
        product = Product.objects.get(id=id)
        product.delete()
        logger.info(f"User {request.user.username} deleted product {product.name}")
        return redirect('dashboard')
    
class EditProductView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.path.startswith('/api/'):
            logger.warning(f"Неавторизованный API доступ: {request.path}")
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id):
        product = Product.objects.get(id=id)
        form = ProductForm(instance=product)
        return render(request, 'main/edit_product.html', {'form': form})
    
    def post(self, request, id):
        product = Product.objects.get(id=id)
        form = ProductForm(request.POST, instance=product)  
        
        if form.is_valid():
            logger.info(f"User {request.user.username} edited product {product.name}")
            form.save() 
            return redirect('dashboard') 
        
        return render(request, 'main/edit_product.html', {'form': form})
    
class EditSupplierView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.path.startswith('/api/'):
            logger.warning(f"Неавторизованный API доступ: {request.path}")
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id):
        supplier = Supplier.objects.get(id=id)
        form = SupplierForm(instance=supplier)
        return render(request, 'main/edit_product.html', {'form': form})
    
    def post(self, request, id):
        supplier = Supplier.objects.get(id=id)
        form = SupplierForm(request.POST, instance=supplier)  
        
        if form.is_valid():
            logger.info(f"User {request.user.username} edited supplier {supplier.name}")
            form.save() 
            return redirect('dashboard') 
        
        return render(request, 'main/edit_product.html', {'form': form})
    
class AddProductView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.path.startswith('/api/'):
            logger.warning(f"Неавторизованный API доступ: {request.path}")
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = ProductForm()
        return render(request, 'main/add_product.html', {'form': form})
    
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            logger.info(f"User {request.user.username} added product {product.name}")
            return redirect('dashboard')
        
class AddSupplierView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.path.startswith('/api/'):
            logger.warning(f"Неавторизованный API доступ: {request.path}")
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = SupplierForm()
        return render(request, 'main/add_supplier.html', {'form': form})
    
    def post(self, request):
        form = SupplierForm(request.POST)
        if form.is_valid():
            supplier = form.save()
            logger.info(f"User {request.user.username} added supplier {supplier.name}")
            return redirect('dashboard')
        
class StatsView(UserPassesTestMixin, LoginRequiredMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated and request.path.startswith('/api/'):
            logger.warning(f"Неавторизованный API доступ: {request.path}")
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        customers = Customer.objects.order_by('user__last_name')
        products = Product.objects.order_by('name')

        sales = Sale.objects.all()
        sale_total = 0
        for sale in sales:
            sale_total += sale.total_price

        seperate_sale_totals = []
        for sale in sales:
            seperate_sale_totals.append(sale.total_price)
        max_sale = max(seperate_sale_totals) if seperate_sale_totals else 1

        sale_stats = {
                'avg': statistics.mean(seperate_sale_totals) if seperate_sale_totals else 0,
                'median': statistics.median(seperate_sale_totals) if seperate_sale_totals else 0,
                'mode': statistics.mode(seperate_sale_totals) if seperate_sale_totals else 0,
                'max_sale': max_sale
            }
        
        # Convert max_value to float for calculations
        max_value = float(max(sale_stats['avg'], sale_stats['median'], sale_stats['mode']))
        y_max = ((max_value // 100) + 1) * 100  # Round up to nearest 100
        
        # Calculate bar heights (0-100%)
        sale_stats['avg_height'] = float(sale_stats['avg']) / y_max * 100
        sale_stats['median_height'] = float(sale_stats['median']) / y_max * 100
        sale_stats['mode_height'] = float(sale_stats['mode']) / y_max * 100

        print(sale_stats['mode_height'])
        
        # Generate Y-axis ticks (using Decimal for consistent formatting)
        y_ticks = [Decimal(str(y_max * (1 - i/4))) for i in range(5)]  # 5 ticks including 0
        
        ages = []
        for customer in customers:
            ages.append(customer.age)

        age_stats = {
            'avg': statistics.mean(ages) if ages else 0,
            'median': statistics.median(ages) if ages else 0
        }    

        popular_category = Category.objects.annotate(
            count=Count('product__sale')
        ).order_by('-count').first()

        profitable_category = Category.objects.annotate(
            profit=Sum(F('product__sale__quantity') * F('product__price'))
        ).order_by('-profit').first()


        return render(request, 'main/stats.html', {'customers': customers,
                                                   'products': products,
                                                   'sale_total': sale_total,
                                                   'sale_stats':sale_stats,
                                                   'age_stats': age_stats,
                                                   'popular_category': popular_category,
                                                   'profitable_category': profitable_category,
                                                    'y_ticks': y_ticks,
                                                    'avg_height': sale_stats['avg_height'],
                                                    'median_height': sale_stats['median_height'],
                                                    'mode_height': sale_stats['mode_height'],})

            


        



