from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.index, name="index"),
    path("index_es", views.index_es, name="index_es"),
    path("about", views.about, name="about"),
    path("about_es", views.about_es, name="about_es"),
    path("services", views.services, name="services"),
    path("services_es", views.services_es, name="services_es"),
    path("portfolio", views.portfolio, name="portfolio"),
    path("portfolio_es", views.portfolio_es, name="portfolio_es"),
    path("contact", views.contact, name="contact"),
    path("contact_es", views.contact_es, name="contact_es"),
    path("faqs", views.faqs, name="faqs"),
    path("faqs_es", views.faqs_es, name="faqs_es"),
    

    ]