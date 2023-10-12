from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=80)
    description = forms.CharField()
    price = forms.FloatField()
    count = forms.IntegerField()
    image = forms.ImageField()
