from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('homepage.urls')),
    path('inventory/', include('inventory.urls')),
    path('transactions/', include('transactions.urls')),
]
