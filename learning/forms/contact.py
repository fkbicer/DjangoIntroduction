from django import forms
from learning.models import Product


class Contact(forms.Form):
    name = forms.CharField(
        label='isim',
        max_length=50,
        min_length=5,
        required=True,
        initial='Isminizi giriniz...',  # form doldurulacak alanın default gösterimi.
        help_text='burası isim yardım metnidir.',
        error_messages={
            'required': 'lutfen isim giriniz',
            'max_length': 'en fazla 50 karakter giriniz.',
            'min_length': 'minimum 5 karakter giriniz.'
        },
        disabled=False,  # True olur ise form görülür ama doldurulamaz.
    )

    email = forms.EmailField(label='Email Adresi')
    content = forms.CharField(widget=forms.Textarea)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
