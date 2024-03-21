from django.urls import reverse
from datetime import datetime
from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import SMRTPROPERTIES, SMRTWEBFORM, PropertyImage, Asociados

 # Create your views here.



def index(request):
    if request.method == 'POST':
        form = SMRTWEBFORMForm(request.POST)
        if form.is_valid():
            form.instance.frm_date = datetime.now()
            form.save()
            # Redirect to a success page or another view after form submission
            return redirect('index')  # Redirect to the same view ('index') after form submission
    else:
        form = SMRTWEBFORMForm()
    
    return render(request, "web_site/index.html", {'form': form})

class SMRTWEBFORMForm(forms.ModelForm):
    frm_fcont = forms.BooleanField(initial=True, required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    
    # Define choices for 'serv' field
    SERVICE_CHOICES = [
        ('Bienes raices - Real State', 'Bienes raices - Real State'),
        ('Inversion - Investment', 'Inversion - Investment'),
        ('Seguros - Insurance', 'Seguros - Insurance'),
        ('Contabilidad - Contability', 'Contabilidad - Contability'),
    ]

    frm_serv = forms.MultipleChoiceField(
        choices=SERVICE_CHOICES,
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),  # Apply Bootstrap class
    )

    class Meta:
        model = SMRTWEBFORM
        exclude = ['frm_date']
        widgets = {
            'frml_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido - Surename'}),
            'frm_fname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre - Name'}),
            'frm_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfon - Telephone'}),
            'frm_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico - Email'}),
            'frm_messag': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Mensaje - Message'}),
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
   asociates = Asociados.objects.filter(activo=True)

   context = {"socios" : asociates       
    } 
   return render(request, "web_site/about.html", context)

def about_es(request):
   asociates = Asociados.objects.filter(activo=True)

   context = {"socios" : asociates       
    } 
   return render(request, "web_site/about_es.html", context)

def services(request):
   return render(request, "web_site/services.html")

def services_es(request):
   return render(request, "web_site/services_es.html")

def real_state_es(request):
   return render(request, "web_site/real_state_es.html")

def smart_investment_es(request):
   return render(request, "web_site/smart_investment_es.html")

def real_state(request):
   return render(request, "web_site/real_state.html")

def smart_investment(request):
   return render(request, "web_site/smart_investment.html")


def contact(request):
   if "data" not in request.session:

        # If not, create a new list
        request.session["data"] = []
   if request.method == 'POST':
      # Take in the data the user submitted and save it as form
      form = SMRTWEBFORMForm(request.POST)
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
      "form": SMRTWEBFORMForm(), "data": request.session["data"]
   })

def portfolio(request):
    # Get images
    imgs = PropertyImage.objects.all()
    # Fetch distinct values for each dropdown
    cities = SMRTPROPERTIES.objects.filter(imb_Active=True).values_list('imb_City', flat=True).distinct()
    property_types = SMRTPROPERTIES.objects.filter(imb_Active=True).values_list('imb_Type', flat=True).distinct()

    # Filter properties based on user input
    active_props = SMRTPROPERTIES.objects.filter(imb_Active=True)

    if request.method == 'GET':
        # Get the filters from the request
        location_filter = request.GET.get('location_filter')  # Filter for location
        property_type_filter = request.GET.get('property_type_filter')  # Filter for property type
        bedroom_filter_min = request.GET.get('bedroom_filter_min')  # Minimum number of bedrooms
        bedroom_filter_max = request.GET.get('bedroom_filter_max')  # Maximum number of bedrooms

        # Apply filters one by one
        if location_filter:
            active_props = active_props.filter(imb_City=location_filter)
        if property_type_filter:
            active_props = active_props.filter(imb_Type=property_type_filter)
        if bedroom_filter_min:
            # Filter properties with number of bedrooms greater than or equal to the minimum specified
            active_props = active_props.filter(imb_Bedrooms__gte=bedroom_filter_min)
        if bedroom_filter_max:
            # Filter properties with number of bedrooms less than or equal to the maximum specified
            active_props = active_props.filter(imb_Bedrooms__lte=bedroom_filter_max)

    # Prepare context to pass to template
    context = {
        "imgs": imgs,  # Pass images
        "props": active_props,  # Pass filtered properties
        "cities": cities,  # Pass city options for dropdown
        "property_types": property_types,  # Pass property type options for dropdown
        "bedroom_filter_min": bedroom_filter_min,  # Pass minimum bedroom filter value
        "bedroom_filter_max": bedroom_filter_max,  # Pass maximum bedroom filter value
    }

    # Render the template with the context
    return render(request, "web_site/portfolio.html", context)


def portfolio_es(request):
    # Obtener imágenes
    imgs = PropertyImage.objects.all()
    # Obtener valores distintos para cada menú desplegable
    cities = SMRTPROPERTIES.objects.filter(imb_Active=True).values_list('imb_City', flat=True).distinct()
    property_types = SMRTPROPERTIES.objects.filter(imb_Active=True).values_list('imb_Type', flat=True).distinct()

    # Filtrar propiedades según la entrada del usuario
    if request.method == 'GET':
        location_filter = request.GET.get('location_filter')
        property_type_filter = request.GET.get('property_type_filter')
        # Agregar más filtros para otros menús desplegables según sea necesario

        active_props = SMRTPROPERTIES.objects.filter(imb_Active=True)
        if location_filter:
            active_props = active_props.filter(imb_City=location_filter)
        if property_type_filter:
            active_props = active_props.filter(imb_Type=property_type_filter)
        # Agregar más filtros para otros menús desplegables según sea necesario

    context = {
        "imgs": imgs,
        "props": active_props,
        "cities": cities,
        "property_types": property_types,
        # Agregar más para otros menús desplegables según sea necesario
    }
    return render(request, "web_site/portfolio_es.html", context)


def contact_es(request):
    form = SMRTWEBFORMForm()  # Define form outside the conditional block
    
    if request.method == 'POST':
        form = SMRTWEBFORMForm(request.POST)
        if form.is_valid():
            form.instance.frm_date = datetime.now()
            form.save()
            return redirect('contact_es')  # Redirect to a success page
    
    return render(request, "web_site/contact_es.html", {'form': form})

def faqs(request):
    return render(request, "web_site/faqs.html")

def faqs_es(request):
    return render(request, "web_site/faqs_es.html")

def insurance_es(request):
   return render(request, "web_site/insurance_es.html")

def accountant_es(request):
   return render(request, "web_site/accountant_es.html")

def insurance(request):
   return render(request, "web_site/insurance.html")

def accountant(request):
   return render(request, "web_site/accountant.html")
