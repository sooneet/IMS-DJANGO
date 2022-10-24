from django.shortcuts import render
from django.views.generic.list import ListView
from . models import Stock
# Create your views here.
class StockListView(ListView):
    model = Stock
    queryset = Stock.objects.filter(is_deleted=False)
    template_name = 'inventory.html'
    paginate_by = 10

