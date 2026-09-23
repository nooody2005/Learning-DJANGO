from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_desc', 'item_price','item_image']
        widgets={
                    "item_name":forms.TextInput(attrs={"placeholder":"e.g Margaretta pizza","required":True}),
                    "item_desc":forms.TextInput(attrs={"placeholder":"e.g Margaretta pizza and Chessy","required":True}),
                    "item_price":forms.NumberInput(attrs={"placeholder":"100","required":True}),
                    "item_image":forms.URLInput(attrs={"placeholder":"http/www.nody.com","required":True})
                }
        