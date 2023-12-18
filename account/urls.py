from django.urls import path
from .views import CustomerRegisterView, CustomerLoginView


urlpatterns = [
    path('customer_register/', CustomerRegisterView.as_view()),
    path('cl/', CustomerLoginView.as_view()),

]