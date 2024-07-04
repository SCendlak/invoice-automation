from django.urls import path

from .views import *
app_name = 'invoice'
urlpatterns = [
    path("", index, name="home"),
    path("generate/", view=upload_pdf, name='invoice'),
    path("show_results/", view=show_results, name='show_results'),
    path('contacts/', view=ContactListView.as_view(), name='contacts'),
    path('contacts/add_contact', add_contact, name='add_contact'),
    path('contact/<str:name>', contact_detail_view, name='contact-details'),
]