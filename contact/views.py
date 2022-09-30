from django.shortcuts import render
from .forms import ContactForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView,FormView
# Create your views here.

class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:success')

    def form_valid(self, form:ContactForm):
        form.send()
        return super().form_valid(form)


class ContactSuccessView(TemplateView):
    template_name = 'contact/success.html'


