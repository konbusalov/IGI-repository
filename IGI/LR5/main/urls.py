from django.urls import path
from .views import *

from django.urls import re_path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$', HomeView.as_view(), name='home'),
    re_path(r'^about/$', AboutView.as_view(), name='about'),
    re_path(r'^news/$', NewsView.as_view(), name='news'),
    re_path(r'^faq/$', FAQView.as_view(), name='faq'),
    re_path(r'^contact/$', ContactView.as_view(), name='contact'),
    re_path(r'^privacy_policy/$', PrivacyPolicyView.as_view(), name='privacy_policy'),
    re_path(r'^jobs/$', JobsView.as_view(), name='jobs'),
    re_path(r'^reviews/$', ReviewsView.as_view(), name='reviews'),
    re_path(r'^promotions/$', PromotionsView.as_view(), name='promotions'),
    re_path(r'^products/$', ProductsView.as_view(), name='products'),
    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
    re_path(r'^register_as_customer/$', RegisterAsCustomerView.as_view(), name='register_as_customer'),
    re_path(r'^register_as_employee/$', RegisterAsEmployeeView.as_view(), name='register_as_employee'),
    re_path(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    re_path(r'^dashboard/purchase_product/(?P<id>\d+)$', PurchaseProductView.as_view(), name='purchase_product'),
    re_path(r'^dashboard/delete_product/(?P<id>\d+)/$', DeleteProductView.as_view(), name='delete_product'),
    re_path(r'^dashboard/delete_supplier/(?P<id>\d+)/$', DeleteSupplierView.as_view(), name='delete_supplier'),
    re_path(r'^dashboard/edit_product/(?P<id>\d+)/$', EditProductView.as_view(), name='edit_product'),
    re_path(r'^dashboard/edit_supplier/(?P<id>\d+)/$', EditSupplierView.as_view(), name='edit_supplier'),
    re_path(r'^dashboard/add_product/$', AddProductView.as_view(), name='add_product'),
    re_path(r'^dashboard/add_supplier/$', AddSupplierView.as_view(), name='add_supplier'),
    re_path(r'^stats/$', StatsView.as_view(), name='stats'),
    path('api/' ,HomeView.as_view(), name='api_home'),
    path('api/about/', AboutView.as_view(), name='api_about'),
    path('api/news/', NewsView.as_view(), name='api_news'),
    path('api/faq/', FAQView.as_view(), name='api_faq'),
    path('api/contact/', ContactView.as_view(), name='api_contact'),
    path('api/privacy_policy/', PrivacyPolicyView.as_view(), name='api_privacy_policy'),
    path('api/jobs/', JobsView.as_view(), name='api_jobs'),
    path('api/reviews/', ReviewsView.as_view(), name='api_reviews'),
    path('api/promotions/', PromotionsView.as_view(), name='api_promotions'),
    path('api/products/', ProductsView.as_view(), name='api_products'),
    path('api/login/', LoginView.as_view(), name='api_login'),
    path('api/logout/', LogoutView.as_view(), name='api_logout'),
    path('api/register/customer/', RegisterAsCustomerView.as_view(), name='api_register_customer'),
    path('api/register/employee/', RegisterAsEmployeeView.as_view(), name='api_register_employee'),
    path('api/dashboard/', DashboardView.as_view(), name='api_dashboard'),
    path('api/dashboard/purchase/<int:id>/', PurchaseProductView.as_view(), name='api_purchase_product'),
    path('api/dashboard/delete/product/<int:id>/', DeleteProductView.as_view(), name='api_delete_product'),
    path('api/dashboard/delete/supplier/<int:id>/', DeleteSupplierView.as_view(), name='api_delete_supplier'),
    path('api/dashboard/edit/product/<int:id>/', EditProductView.as_view(), name='api_edit_product'),
    path('api/dashboard/edit/supplier/<int:id>/', EditSupplierView.as_view(), name='api_edit_supplier'),
    path('api/dashboard/add/product/', AddProductView.as_view(), name='api_add_product'),
    path('api/dashboard/add/supplier/', AddSupplierView.as_view(), name='api_add_supplier'),
    path('api/stats/', StatsView.as_view(), name='api_stats'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
