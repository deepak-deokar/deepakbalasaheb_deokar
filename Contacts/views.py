
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from .models import Contact
from .forms import ContactForm

class ContactListView(ListView):
    model = Contact
    template_name = 'Contact_list.html'

class ContactCreateView(CreateView):
    model = Contact
    template_name = 'Contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('Contacts:contact_list')

class ContactUpdateView(UpdateView):
    model = Contact
    template_name = 'Contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('Contacts:contact_list')

class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'Contact_confirm_delete.html'
    success_url = reverse_lazy('Contacts:contact_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        contact_name = self.object.name  
        response = super(ContactDeleteView, self).delete(request, *args, **kwargs)
        success_message = f'"{self.object.name}" has been successfully deleted.'
        messages.success(request, success_message)
        return response

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'Contact_detail.html'

