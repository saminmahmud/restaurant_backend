from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/', include('food.urls')),
    path('category/', include('categories.urls')),
    path('review/', include('review.urls')),
    path('account/', include('account.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)