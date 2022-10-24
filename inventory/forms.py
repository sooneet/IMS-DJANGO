from django import forms
from . models import Stock

class StockFrom(forms.ModelForm):
    def __in__(self,*args,**kwargs):
        super().init__(*args,**kwargs)
        self.fields['name'].widget.attrs.update({'class':'textinput form-control'})
        self.fields['quantity'].widget.attrs.update({'class':'textinput form-control','min':'0'})

    class Meta:
        model = Stock
        fields = ['name','quantity']        