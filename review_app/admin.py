from django.contrib import admin
from .models import Category, Product,Cart,ProductReview, Wichlist

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(ProductReview)
admin.site.register(Wichlist)
