from django.urls import path
from . import views
urlpatterns = [path('contact/', views.ContactView.as_view(), name='contact'),
               path('contact/mail/', views.SendContact.as_view(), name='send_message'),
               path('contact/success/', views.Success.as_view(), name='success_page'),
               ]