from django import forms

from accounts.models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['profile', 'amount', 'transaction_code']
