from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

class RawProductForm(forms.Form):
    #WE DON'T HAVE TEXT FIELD HERE
    #FORM FIELD IS DEFERENT FROM MODEL FIELD
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'your title'}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                    'placeholder': 'your description',
                    'class': 'new-class-name two',
                    'id':'my-id-for-textarea',
                    'rows': 10,
                    'cols': 70
                   }
        )
    )
    price = forms.DecimalField(initial=199.99)