from django import forms


class ShowTimeSearchForm(forms.Form):
    movie_name = forms.CharField(max_length=100, label='عنوان فیلم',required=False)
