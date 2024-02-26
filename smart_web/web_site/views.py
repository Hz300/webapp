from django.urls import reverse
from datetime import datetime
from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import SMRTPROPERTIES, SMRTWEBFORM

 # Create your views here.



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

class SMRTWEBFORMForm(forms.ModelForm):
    frm_fcont = forms.BooleanField(initial=True, required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    
    class Meta:
        model = SMRTWEBFORM
        exclude = ['frm_date']
        widgets = {
            'frml_name': forms.TextInput(attrs={'class': 'form-control'}),
            'frm_fname': forms.TextInput(attrs={'class': 'form-control'}),
            'frm_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'frm_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'frm_serv': forms.TextInput(attrs={'class': 'form-control'}),
            'frm_messag': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

def index_es(request):
    if request.method == 'POST':
        form = SMRTWEBFORMForm(request.POST)
        if form.is_valid():
            form.instance.frm_date = datetime.now()
            form.save()
            return redirect('index_es')  # Redirect to a success page
    else:
        form = SMRTWEBFORMForm()
    
    return render(request, "web_site/index_es.html", {'form': form})

def about(request):
   return render(request, "web_site/about.html")

def about_es(request):
   return render(request, "web_site/about_es.html")

def services(request):
   return render(request, "web_site/services.html")

def services_es(request):
   return render(request, "web_site/services_es.html")

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

def portfolio(request):
   return render(request, "web_site/portfolio.html",{
      "props": SmrtProperties.objects.all()
   })

def portfolio_es(request):
   return render(request, "web_site/portfolio_es.html",{
      "props": SmrtProperties.objects.all()
   })

def contact_es(request):
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
         return HttpResponseRedirect(reverse("contact_es"))
      else:

            # If the form is invalid, re-render the page with existing information.
            return render(request, "web_site/contact_es.html", {
                "form": form, "data": request.session["data"]
            })

   return render(request, "web_site/contact_es.html", {
      "form": ContactForm(), "data": request.session["data"]
   })


def faqs(request):
    return render(request, "web_site/faqs.html")

def faqs_es(request):
    return render(request, "web_site/faqs_es.html")