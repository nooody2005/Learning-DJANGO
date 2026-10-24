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


    def clean_item_price(self):
        price = self.cleaned_data["item_price"]
        if price<0:
            raise forms.ValidationError("Price Can't be negative")
        return price


    def clean(self):
        cleaned = super().clean()
        name = cleaned.get("item_name")
        desc = cleaned.get("item_desc")
        if name and desc and name.lower() in desc.lower():
            self.add_error("item_desc","Description should add new info beyond the name")
        return cleaned