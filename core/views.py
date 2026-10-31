
from django.shortcuts import render, get_object_or_404, redirect
from urllib.parse import quote

from .models import WebsiteProduct
from .forms import WebsiteOrderForm


def home(request):
    websites = WebsiteProduct.objects.filter(
        status='available'
    ).order_by('-created_at')

    return render(request, 'core/home.html', {
        'websites': websites
    })


def checkout(request, pk):
    website = get_object_or_404(
        WebsiteProduct,
        pk=pk,
        status='available'
    )

    if request.method == 'POST':
        form = WebsiteOrderForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.website = website
            order.payment_method = 'whatsapp'
            order.save()

            number = '923495311678'

            message = (
                f"Website Order\n"
                f"Website: {website.name}\n"
                f"Price: PKR {website.price}\n"
                f"Customer: {order.customer_name}\n"
                f"Phone: {order.phone}\n"
                f"Email: {order.email}"
            )

            whatsapp_url = (
                f"https://wa.me/{number}?text={quote(message)}"
            )

            return redirect(whatsapp_url)

    else:
        form = WebsiteOrderForm()

    return render(request, 'core/checkout.html', {
        'website': website,
        'form': form
    })

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if not name or not email or not message:
            return render(request, 'core/contact.html', {
                'error': 'Please fill in all fields.'
            })

        number = '923495311678'

        whatsapp_message = (
            f"New Portfolio Contact\n"
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Message: {message}"
        )

        whatsapp_url = (
            f"https://wa.me/{number}?text={quote(whatsapp_message)}"
        )

        return redirect(whatsapp_url)

    return render(request, 'core/contact.html')
