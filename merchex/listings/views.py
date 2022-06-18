from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect

from listings.models import Band
from listings.models import Title
from listings.forms import ContactUsForm


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html',
                  {'bands': bands})


def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html',
                  {'band': band})


def about(request):
    return render(request, 'listings/about.html')


def listings_list(request):
    titles = Title.objects.all()
    return render(request, 'listings/listings_list.html',
                  {'titles': titles})


def listings_detail(request, id):
    title = Title.objects.get(id=id)
    return render(request, 'listings/listings_detail.html',
                  {'title': title})


def contact(request):
    #print('La méthode de requête est : ', request.method)
    #print('Les données POST sont : ', request.POST)

    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f"Message from {form.cleaned_data['name'] or 'anonyme'} via MerchEx Contact Us form",
                message=form.cleaned_data["message"],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz']
            )
        return redirect('email_sent.html')
    else:
        form = ContactUsForm()

    return render(request, 'listings/contact.html',
                  {'form': form})


def email_sent(request):
    return render(request, 'listings/email_sent.html')