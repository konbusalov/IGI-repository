from django.contrib import admin
from .models import *

class ProductInline(admin.TabularInline):
    model = Product.suppliers.through
    extra = 1

# First register all models with their custom admin classes
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ('name', 'address')
    list_filter = ('name',)
    inlines = [ProductInline]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'article', 'price', 'category', 'quantity')
    list_filter = ('category', 'suppliers', 'price')
    search_fields = ('name', 'article')
    filter_horizontal = ('suppliers',)
    raw_id_fields = ('category',)

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'customer', 'date', 'quantity', 'total_price')
    list_filter = ('date', 'product', 'customer')
    search_fields = ('product__name', 'customer__user__username')
    date_hierarchy = 'date'
    readonly_fields = ('total_price',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('author__username', 'text')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'age')
    search_fields = ('user__username', 'phone')
    list_filter = ('age',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'phone', 'age')
    search_fields = ('user__username', 'position', 'phone')
    list_filter = ('position', 'age')

@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'is_active', 'valid_until')
    list_filter = ('is_active', 'valid_until')
    search_fields = ('code',)

# Basic registration for models that don't need customization
admin.site.register(CompanyInfo)
admin.site.register(Article)
admin.site.register(FAQ)
admin.site.register(JobOpening)
admin.site.register(Category)

