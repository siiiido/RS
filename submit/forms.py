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

class PollsForm(forms.Form):
    Q01 = forms.BooleanField(label='Q01')
    Q02 = forms.BooleanField(label='Q02')
    Q03 = forms.BooleanField(label='Q03')
    Q04 = forms.BooleanField(label='Q04')
    Q05 = forms.BooleanField(label='Q05')
    Q06 = forms.BooleanField(label='Q06')
    Q07 = forms.BooleanField(label='Q07')
    Q08 = forms.BooleanField(label='Q08')
    Q09 = forms.BooleanField(label='Q09')
    Q10 = forms.BooleanField(label='Q10')

    