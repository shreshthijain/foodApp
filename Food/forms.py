from django import forms
from .models import Item

class AddItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_description', 'item_price', 'item_image', 'item_category']
        