from django.contrib.auth import get_user_model
from django.db import models

GENDER={
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Prefer not to say', 'Prefer not to say'),
}


class Customer(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    first_name = models.CharField(max_length= 200, blank= False)
    last_name = models.CharField(max_length= 200, blank=False)
   # email = models.EmailField(max_length= 200)
    phone_number = models.CharField(max_length= 12)
    city = models.CharField(max_length= 20)
    address = models.CharField(max_length= 200)
    gender = models.CharField(max_length= 17, choices=GENDER, default='Prefer not to say')


    def __str__(self):
        return self.first_name+' '+self.last_name
