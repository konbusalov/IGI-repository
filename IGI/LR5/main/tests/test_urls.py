from django.test import TestCase
from django.urls import reverse, resolve
from main.views import *

class URLTests(TestCase):
    def test_home_url(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, HomeView)

    def test_about_url(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func.view_class, AboutView)

    def test_news_url(self):
        url = reverse('news')
        self.assertEqual(resolve(url).func.view_class, NewsView)

    def test_faq_url(self):
        url = reverse('faq')
        self.assertEqual(resolve(url).func.view_class, FAQView)

    def test_contact_url(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func.view_class, ContactView)

    def test_privacy_policy_url(self):
        url = reverse('privacy_policy')
        self.assertEqual(resolve(url).func.view_class, PrivacyPolicyView)

    def test_jobs_url(self):
        url = reverse('jobs')
        self.assertEqual(resolve(url).func.view_class, JobsView)

    def test_reviews_url(self):
        url = reverse('reviews')
        self.assertEqual(resolve(url).func.view_class, ReviewsView)

    def test_promotions_url(self):
        url = reverse('promotions')
        self.assertEqual(resolve(url).func.view_class, PromotionsView)

    def test_products_url(self):
        url = reverse('products')
        self.assertEqual(resolve(url).func.view_class, ProductsView)

    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, LoginView)

    def test_logout_url(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, LogoutView)

    def test_register_customer_url(self):
        url = reverse('register_as_customer')
        self.assertEqual(resolve(url).func.view_class, RegisterAsCustomerView)

    def test_register_employee_url(self):
        url = reverse('register_as_employee')
        self.assertEqual(resolve(url).func.view_class, RegisterAsEmployeeView)

    def test_dashboard_url(self):
        url = reverse('dashboard')
        self.assertEqual(resolve(url).func.view_class, DashboardView)

    def test_purchase_product_url(self):
        url = reverse('purchase_product', args=[1])
        self.assertEqual(resolve(url).func.view_class, PurchaseProductView)

    def test_delete_product_url(self):
        url = reverse('delete_product', args=[1])
        self.assertEqual(resolve(url).func.view_class, DeleteProductView)

    def test_delete_supplier_url(self):
        url = reverse('delete_supplier', args=[1])
        self.assertEqual(resolve(url).func.view_class, DeleteSupplierView)

    def test_edit_product_url(self):
        url = reverse('edit_product', args=[1])
        self.assertEqual(resolve(url).func.view_class, EditProductView)

    def test_edit_supplier_url(self):
        url = reverse('edit_supplier', args=[1])
        self.assertEqual(resolve(url).func.view_class, EditSupplierView)

    def test_add_product_url(self):
        url = reverse('add_product')
        self.assertEqual(resolve(url).func.view_class, AddProductView)

    def test_add_supplier_url(self):
        url = reverse('add_supplier')
        self.assertEqual(resolve(url).func.view_class, AddSupplierView)

    def test_stats_url(self):
        url = reverse('stats')
        self.assertEqual(resolve(url).func.view_class, StatsView)

    def test_api_home_url_resolves(self):
        url = reverse('api_home')
        self.assertEqual(resolve(url).func.view_class, HomeView)

    def test_api_about_url_resolves(self):
        url = reverse('api_about')
        self.assertEqual(resolve(url).func.view_class, AboutView)

    def test_api_news_url_resolves(self):
        url = reverse('api_news')
        self.assertEqual(resolve(url).func.view_class, NewsView)

    def test_api_faq_url_resolves(self):
        url = reverse('api_faq')
        self.assertEqual(resolve(url).func.view_class, FAQView)

    def test_api_contact_url_resolves(self):
        url = reverse('api_contact')
        self.assertEqual(resolve(url).func.view_class, ContactView)

    def test_api_privacy_policy_url_resolves(self):
        url = reverse('api_privacy_policy')
        self.assertEqual(resolve(url).func.view_class, PrivacyPolicyView)

    def test_api_jobs_url_resolves(self):
        url = reverse('api_jobs')
        self.assertEqual(resolve(url).func.view_class, JobsView)

    def test_api_reviews_url_resolves(self):
        url = reverse('api_reviews')
        self.assertEqual(resolve(url).func.view_class, ReviewsView)

    def test_api_promotions_url_resolves(self):
        url = reverse('api_promotions')
        self.assertEqual(resolve(url).func.view_class, PromotionsView)

    def test_api_products_url_resolves(self):
        url = reverse('api_products')
        self.assertEqual(resolve(url).func.view_class, ProductsView)

    def test_api_login_url_resolves(self):
        url = reverse('api_login')
        self.assertEqual(resolve(url).func.view_class, LoginView)

    def test_api_logout_url_resolves(self):
        url = reverse('api_logout')
        self.assertEqual(resolve(url).func.view_class, LogoutView)

    def test_api_register_customer_url_resolves(self):
        url = reverse('api_register_customer')
        self.assertEqual(resolve(url).func.view_class, RegisterAsCustomerView)

    def test_api_register_employee_url_resolves(self):
        url = reverse('api_register_employee')
        self.assertEqual(resolve(url).func.view_class, RegisterAsEmployeeView)

    def test_api_dashboard_url_resolves(self):
        url = reverse('api_dashboard')
        self.assertEqual(resolve(url).func.view_class, DashboardView)

    def test_api_purchase_product_url_resolves(self):
        url = reverse('api_purchase_product', args=[1])
        self.assertEqual(resolve(url).func.view_class, PurchaseProductView)

    def test_api_delete_product_url_resolves(self):
        url = reverse('api_delete_product', args=[1])
        self.assertEqual(resolve(url).func.view_class, DeleteProductView)

    def test_api_delete_supplier_url_resolves(self):
        url = reverse('api_delete_supplier', args=[1])
        self.assertEqual(resolve(url).func.view_class, DeleteSupplierView)

    def test_api_edit_product_url_resolves(self):
        url = reverse('api_edit_product', args=[1])
        self.assertEqual(resolve(url).func.view_class, EditProductView)

    def test_api_edit_supplier_url_resolves(self):
        url = reverse('api_edit_supplier', args=[1])
        self.assertEqual(resolve(url).func.view_class, EditSupplierView)

    def test_api_add_product_url_resolves(self):
        url = reverse('api_add_product')
        self.assertEqual(resolve(url).func.view_class, AddProductView)

    def test_api_add_supplier_url_resolves(self):
        url = reverse('api_add_supplier')
        self.assertEqual(resolve(url).func.view_class, AddSupplierView)

    def test_api_stats_url_resolves(self):
        url = reverse('api_stats')
        self.assertEqual(resolve(url).func.view_class, StatsView)

    def test_url_response_codes(self):
        # Test public URLs that should return 200
        public_urls = [
            reverse('home'),
            reverse('about'),
            reverse('news'),
            reverse('faq'),
            reverse('contact'),
            reverse('privacy_policy'),
            reverse('jobs'),
            reverse('reviews'),
            reverse('promotions'),
            reverse('products'),
            reverse('login'),
        ]
        
        for url in public_urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    def test_protected_url_redirects(self):
        # Test URLs that should redirect if not logged in
        protected_urls = [
            reverse('dashboard'),
            reverse('add_product'),
            reverse('add_supplier'),
            reverse('stats'),
        ]
        
        for url in protected_urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)