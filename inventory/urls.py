from django.urls import path
from . import views


urlpatterns = [
    path('',views.StockListView.as_view(),name='inventory'),
    path('new/',views.StockCreateView.as_view(),name='new-stock'),
    path('stock/<int:pk>/edit/',views.StockUpdateView.as_view(),name='edit-stock'),
]
