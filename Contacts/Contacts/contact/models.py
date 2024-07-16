from django.db import models

class CONTACT(models.Model): 
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=150)
    address = models.TextField(max_length=150)

    def __str__(self):
        return self.name
