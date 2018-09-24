from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.


def contact(request):
    # print("Tipode peticion {}".format(request.method))
    contact_form = ContactForm
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            # enviar correo y redireccionar
            email = EmailMessage(
                'La caffettiera: nuevo mensaje de contacto',
                'de {} <{}>\n\n Escribio:\n\n{}'.format(name,email,content),
                'no-contestar@inbox.mailtrap.io',
                ["ivanrojo07@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+'?ok')
                
            except:
                return redirect(reverse('contact')+'?fail')
    return render(request, 'contact/contact.html',{'form':contact_form})
