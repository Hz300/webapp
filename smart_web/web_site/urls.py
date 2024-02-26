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
    path("real_state_es", views.real_state_es, name="real_state_es"),
    path("smart_investment_es", views.smart_investment_es, name="smart_investment_es"),
    path("insurance_es", views.insurance_es, name="insurance_es"),
    path("accountant_es", views.accountant_es, name="accountant_es"),

    ]