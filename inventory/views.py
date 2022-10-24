from django.shortcuts import render
from django.views.generic import ListView,CreateView
from django.contrib.messages.views import SuccessMessageMixin
from . models import Stock
from . forms import StockFrom
# Create your views here.
class StockListView(ListView):
    model = Stock
    queryset = Stock.objects.filter(is_deleted=False)
    template_name = 'inventory.html'
    paginate_by = 10


class StockCreateView(CreateView,SuccessMessageMixin):
    model = Stock
    form_class = StockFrom
    template_name = 'edit_stock.html'
    success_url = '/inventory'
    success_messages = 'Stock has been created successfully'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Stock'
        context['savebtn'] = 'Add to Inventory'
        return context

