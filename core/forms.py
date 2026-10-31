
from django import forms
from .models import WebsiteOrder


class WebsiteOrderForm(forms.ModelForm):

    class Meta:
        model = WebsiteOrder

        fields = [
            'customer_name',
            'email',
            'phone',
            'message',
        ]

        widgets = {
            'customer_name': forms.TextInput(
                attrs={'placeholder': 'Your Name'}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Your Email'}
            ),
            'phone': forms.TextInput(
                attrs={'placeholder': 'WhatsApp Number'}
            ),
            'message': forms.Textarea(
                attrs={'placeholder': 'Your requirements', 'rows': 4}
            ),
        }
