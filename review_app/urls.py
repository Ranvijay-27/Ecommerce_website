from unicodedata import name
from xml.dom.minidom import Document
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='index'),
    path('main',views.main,name='main'), 
    path('colections',views.colections,name='colections'), 
    path('colections/<str:slug>',views.colectionsview,name = 'colectionsview'),
    path('colections/<str:cate_slug>/<str:prod_slug>',views.productview,name='productview'),
    # path('view',views.view,name = view)showreview
    path('showreview',views.showreview,name = 'showreview'),
    path('register',views.register,name = 'register'),
    path('login',views.loginpage,name = 'loginpage'),
    path('logout',views.logoutpage,name = 'logout'),
    path('addtocart',views.addtocart,name = 'addtocart'),
    path('cart',views.cart,name = 'cart'),
    path('checkout',views.checkout,name = 'checkout'),
    path('details',views.details,name = 'details'),
    path('success1',views.success1,name = 'success1'),
    path('proceed-to-pay',views.razorpaycheck,name = 'razorpaycheck'),
    path('mails',views.mails,name = 'mails'),
    path('product-list',views.productlistAjax,name = 'productlist'),
    path('product-price',views.productpriceAjax,name = 'productprice'),
    path('searchproduct',views.searchproduct,name = 'searchproduct'),
    path('saveReview',views.save_review,name = 'saveReview'),
    path('review-rating',views.savereview,name = 'review-rating'),
    path('poPup',views.popup,name = 'poPup'),
    path('wishlist',views.wishlist,name = 'wishlist'),
    path('add-To-wishlist',views.addtowishlist,name = 'addtowishlist'),
    path('update-cart',views.updatecart,name = 'updatecart'),
    path('update-product',views.updateproduct,name='updateproduct'),
    path('delete-cart-item',views.deletecartitem,name = 'deletecartitem'),
    path('price_check',views.pricecheck,name = 'price_check')
   
   
    
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)   
