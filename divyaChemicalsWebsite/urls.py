from unicodedata import name
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('',views.home,name="home"),  
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('blogs/',views.blogs,name="blogs"),
    path('blogs/<str:title>',views.blogView,name="blog-view"),
    path('products/<str:type>',views.productss,name="products"),
    path('products/electrical/<str:type>',views.productInfo,name="electrical"),
    path('products/mechanical/<str:type>',views.productInfo,name="mechanical"),
    path('products/civil/<str:type>',views.productInfo,name="civil"),
    path('productInfo/',views.productInfo,name="productInfo"),

    path('downloads/',views.downloads,name="downloads"),
    path('portfolio/',views.portfolio,name="portfolio"),
 
    path('home/',views.querySet,name='contactQuery')
    ]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)