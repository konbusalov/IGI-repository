from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from django.urls import reverse
from django.utils import timezone
import pytz
from main.models import Article, Customer, Employee, FAQ, JobOpening, Review, PromoCode, Product, Category, Sale, Supplier
from main.views import *
from django.contrib.messages import get_messages
from main.forms import UserForm, CustomerForm, EmployeeForm


class ViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        
        # Create users
        self.user = User.objects.create_user(   
            username='testuser', 
            password='pbkdf2_sha256$1000000$6nqQi7EN8jzttxaA1dOGJi$DOwiW5iUSRz4ANfLdmgSlk7tPAlklB/NPBrKOioiT9w=',
            first_name='Test',
            last_name='User'
        )
        self.employee_user = User.objects.create_user(
            username='employee', 
            password='employeepass',
            first_name='Employee',
            last_name='Test'
        )
        
        # Create categories
        self.category = Category.objects.create(
            name='Electronics',
            description='Electronic devices'
        )
        
        # Create suppliers
        self.supplier = Supplier.objects.create(
            name='Test Supplier',
            address='123 Test St, Test City',
            phone='+375 (29) 123-45-67'
        )
        
        # Create products
        self.product = Product.objects.create(
            article='TEST123',
            name='Test Product',
            price=50.00,
            category=self.category,
            quantity=100
        )
        self.expensive_product = Product.objects.create(
            article='EXP123',
            name='Expensive Product',
            price=100.00,
            category=self.category,
            quantity=5
        )
        self.cheap_product = Product.objects.create(
            article='CHP123', 
            name='Cheap Product',
            price=20.00,
            category=self.category,
            quantity=10
        )
        self.product.suppliers.add(self.supplier)
        
        # Create customers and employees
        self.customer = Customer.objects.create(
            user=self.user,
            phone='+375 (29) 765-43-21',
            age=25
        )
        
        self.employee = Employee.objects.create(
            user=self.employee_user,
            position='Manager',
            phone='+375 (33) 987-65-43',
            age=30,
            responsibilities='Manage everything'
        )
        
        # Create sales
        self.sale = Sale.objects.create(
            product=self.product,
            customer=self.customer,
            quantity=2
        )
        
        # Create articles
        self.article = Article.objects.create(
            title='Test Article',
            summary='Test Summary',
            content='Test Content',
            pub_date=timezone.now()
        )
        
        # Create FAQs
        self.faq = FAQ.objects.create(
            question='Test Question',
            answer='Test Answer'
        )
        
        # Create job openings
        self.job = JobOpening.objects.create(
            title='Test Job',
            description='Test Description',
            requirements='Test Requirements',
            salary='1000 USD'
        )
        
        # Create promo codes
        self.promo = PromoCode.objects.create(
            code='TESTCODE',
            discount=10,
            is_active=True,
            valid_until=timezone.now().date() + timezone.timedelta(days=7)
        )
        
        # Create reviews
        self.review = Review.objects.create(
            author=self.user,
            rating=5,
            text='Great product!'
        )

    def test_home_view(self):
        request = self.factory.get('/')
        request.user = self.user
        response = HomeView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_home_view_with_anonymous_user(self):
        request = self.factory.get('/')
        request.user = AnonymousUser()
        response = HomeView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_about_view(self):
        request = self.factory.get('/about/')
        request.user = AnonymousUser() 
        response = AboutView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_news_view(self):
        request = self.factory.get('/news/')
        request.user = AnonymousUser() 
        response = NewsView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_faq_view(self):
        request = self.factory.get('/faq/')
        request.user = AnonymousUser() 
        response = FAQView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_contact_view(self):
        request = self.factory.get('/contact/')
        request.user = AnonymousUser() 
        response = ContactView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    # Test API data in home view
    def test_home_view_with_api_data(self):
        request = self.factory.get('/')
        request.user = self.user
        response = HomeView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        # Can't test actual API responses as they're random, but we can test the view handles them

    def test_news_view_empty(self):
        Article.objects.all().delete()
        request = self.factory.get('/news/')
        request.user = AnonymousUser() 
        response = NewsView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_privacy_policy_view(self):
        request = self.factory.get('/privacy_policy/')
        request.user = AnonymousUser() 
        response = PrivacyPolicyView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_jobs_view(self):
        request = self.factory.get('/jobs/')
        request.user = AnonymousUser() 
        response = JobsView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_reviews_view_get(self):
        request = self.factory.get('/reviews/')
        request.user = self.user
        response = ReviewsView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_reviews_view_post(self):
        request = self.factory.post('/reviews/', {
            'rating': 4,
            'text': 'Good experience'
        })
        request.user = self.user
        response = ReviewsView.as_view()(request)
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertEqual(Review.objects.count(), 2)

    def test_promotions_view(self):
        request = self.factory.get('/promotions/')
        request.user = AnonymousUser() 
        response = PromotionsView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_products_view(self):
        request = self.factory.get('/products/')
        request.user = AnonymousUser() 
        response = ProductsView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_products_view_filtering(self):
        # Test category filter
        response = self.client.get('/products/?category=' + str(self.category.id))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')  # Should find our test product
        self.assertContains(response, 'Expensive Product')
        self.assertContains(response, 'Cheap Product')

        # Test min price filter
        response = self.client.get('/products/?min_price=50')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Expensive Product')
        self.assertNotContains(response, 'Cheap Product')

        # Test max price filter
        response = self.client.get('/products/?max_price=50')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Cheap Product')
        self.assertNotContains(response, 'Expensive Product')

        # Test search
        response = self.client.get('/products/?search=Expensive')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Expensive Product')
        self.assertNotContains(response, 'Cheap Product')

        # Test price ascending sort
        response = self.client.get('/products/?sort=price_asc')
        self.assertEqual(response.status_code, 200)
        # Get the product names in order they appear in response
        product_names = [prod.name for prod in response.context['products']]
        self.assertEqual(product_names, ['Cheap Product', 'Test Product', 'Expensive Product'])

        # Test price descending sort
        response = self.client.get('/products/?sort=price_desc')
        self.assertEqual(response.status_code, 200)
        product_names = [prod.name for prod in response.context['products']]
        self.assertEqual(product_names, ['Expensive Product', 'Test Product', 'Cheap Product'])

    def test_login_view_get(self):
        request = self.factory.get('/login/')
        request.user = AnonymousUser() 
        response = LoginView.as_view()(request)
        self.assertEqual(response.status_code, 200)


    # Registration Tests
    def test_register_as_customer_view_get(self):
        request = self.factory.get('/register_as_customer/')
        request.user = AnonymousUser() 
        response = RegisterAsCustomerView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_register_as_employee_view_get(self):
        request = self.factory.get('/register_as_employee/')
        request.user = AnonymousUser() 
        response = RegisterAsEmployeeView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_employee(self):
        request = self.factory.get('/dashboard/')
        request.user = self.employee_user
        response = DashboardView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_customer(self):
        request = self.factory.get('/dashboard/')
        request.user = self.user
        response = DashboardView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_anonymous(self):
        request = self.factory.get('/dashboard/')
        request.user = AnonymousUser()
        response = DashboardView.as_view()(request)
        self.assertEqual(response.status_code, 302) 

    def test_api_home_unauthenticated(self):
        request = self.factory.get('/api/')
        request.user = AnonymousUser()
        response = HomeView.as_view()(request)
        self.assertEqual(response.status_code, 401)

    def test_api_home_authenticated(self):
        request = self.factory.get('/api/')
        request.user = self.user
        response = HomeView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_api_register_employee_authenticated(self):
        request = self.factory.get('/api/register/employee/')
        request.user = self.user
        response = RegisterAsEmployeeView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_api_register_customer_authenticated(self):
        request = self.factory.get('/api/register/customer/')
        request.user = self.user
        response = RegisterAsCustomerView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_api_dashboard_superuser(self):
        self.user.is_superuser = True
        self.user.save()
        request = self.factory.get('/api/dashboard/')
        request.user = self.user
        response = DashboardView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_api_dashboard_employee(self):
        request = self.factory.get('/api/dashboard/')
        request.user = self.employee_user
        response = DashboardView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_api_purchase_product(self):
        request = self.factory.post('/api/dashboard/purchase/1/', {'quantity': 1})
        request.user = self.user
        response = PurchaseProductView.as_view()(request, id=1)
        self.assertEqual(response.status_code, 302)