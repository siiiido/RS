from django import forms


class KakaoForm(forms.Form):
    name = forms.CharField(label='name', max_length=20)
    gender = forms.CharField(label='gender', max_length=5)
    birth = forms.IntegerField(label='birth')

class UserForm(forms.Form):
    contact = forms.CharField(label='contact', max_length=30)
    university = forms.CharField(label='university', max_length=30)
    image = forms.ImageField(label='image')
    preference = forms.IntegerField(label='preference')
