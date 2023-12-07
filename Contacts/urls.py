# Contacts/urls.py
from django.urls import path
from .views import ContactListView, ContactCreateView, ContactUpdateView, ContactDeleteView, ContactDetailView

app_name = 'Contacts'

urlpatterns = [
    path('', ContactListView.as_view(), name='contact_list'),
    path('new/', ContactCreateView.as_view(), name='contact_create'),
    path('<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),
    path('<int:pk>/edit/', ContactUpdateView.as_view(), name='contact_edit'),
    path('<int:pk>/delete/', ContactDeleteView.as_view(), name='contact_delete'),
]
