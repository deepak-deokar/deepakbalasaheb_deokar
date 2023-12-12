from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Contact
from .forms import ContactForm

class ContactListView(ListView):
    model = Contact
    template_name = 'Contact_list.html'

class ContactCreateView(CreateView):
    model = Contact
    template_name = 'Create_contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('Contacts:contact_list')

class ContactUpdateView(UpdateView):
    model = Contact
    template_name = 'Update_contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('Contacts:contact_list')

class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'Contact_confirm_delete.html'
    success_url = reverse_lazy('Contacts:contact_list')

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'Contact_detail.html'
