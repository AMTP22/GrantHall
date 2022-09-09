
from .models import Item, Order

from django import forms



class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'
        
class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'
