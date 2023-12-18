from django.contrib import admin

# Register your models here.
from account.models import Customer

admin.site.register(Customer)