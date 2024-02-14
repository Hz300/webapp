from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from .models import SmrtProperties

 # Create your views here.

class NewsletterForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    phone_number = forms.CharField(label='Phone Number', max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
    service = forms.ChoiceField(label='Select Service', choices=(('Service 1', 'Service 1'), ('Service 2', 'Service 2'), ('Service 3', 'Service 3')), widget=forms.Select(attrs={'class': 'form-control wide', 'placeholder': 'Select Service'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': 'message-box form-control', 'placeholder': 'Message'}))

def handle_subscription(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Process the email (save to database, etc.)
            # Redirect to a success page or any other desired page
            return HttpResponseRedirect(reverse('index'))
    else:
        form = NewsletterForm()

    return render(request, 'web_site/subscription.html', {'form': form})

def index(request):
   if "data" not in request.session:

        # If not, create a new list
        request.session["data"] = []
   #comprobar que se esta enviando este formulario y no otro     
   if 'Subscribe' in request.POST:
      # Take in the data the user submitted and save it as form
      form = ContactForm(request.POST)
       # Check if form data is valid (server-side)
      if form.is_valid():
         user = form.cleaned_data
         request.session["data"] += [user]
         return HttpResponseRedirect(reverse("index"))
      else:

            # If the form is invalid, re-render the page with existing information.
            return render(request, "web_site/index.html", {
                "form": form, "data": request.session["data"]
            })
   return render(request, "web_site/index.html", {
      "form": ContactForm(), 
   })

def about(request):
   return render(request, "web_site/about.html")

def services(request):
   return render(request, "web_site/services.html")

def portfolio(request):
   return render(request, "web_site/portfolio.html",{
      "props": SmrtProperties.objects.all()
   })

def contact(request):
   if "data" not in request.session:

        # If not, create a new list
        request.session["data"] = []
   if request.method == 'POST':
      # Take in the data the user submitted and save it as form
      form = ContactForm(request.POST)
       # Check if form data is valid (server-side)
      if form.is_valid():
         user = form.cleaned_data
         request.session["data"] += [user]
         return HttpResponseRedirect(reverse("contact"))
      else:

            # If the form is invalid, re-render the page with existing information.
            return render(request, "tasks/add.html", {
                "form": form, "data": request.session["data"]
            })

   return render(request, "web_site/contact.html", {
      "form": ContactForm(), "data": request.session["data"]
   })

def faqs(request):
    return render(request, "web_site/faqs.html")