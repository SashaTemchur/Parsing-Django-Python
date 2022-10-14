from django.db import models

from django.db import models

class ClientsList(models.Model):
    # Creates a model that will contain the entire list of customers
    full_name = models.CharField('Full name', max_length=500)
    email = models.CharField('Email', max_length=500)
    address = models.CharField('Address', max_length=500)
    phone_number = models.CharField('Phone', max_length=500)
    current_balance = models.FloatField('Balance')
    last_payment = models.DateTimeField('Last payment')
    reg_date = models.DateTimeField('Data')
    lastcall_date = models.DateTimeField('Last call')
    status = models.BooleanField('Status')
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "client"
        verbose_name_plural= "clients"


class InactiveClients(models.Model):
    # Creates a model in which there will be a list of inactive clients
    full_name = models.CharField('Full name', max_length=500)
    email = models.CharField('Email', max_length=500)
    address = models.CharField('Address', max_length=500)
    phone_number = models.CharField('Phone', max_length=500)
    current_balance = models.FloatField('Balance')
    last_payment = models.DateTimeField('Last payment')
    reg_date = models.DateTimeField('Data')
    lastcall_date = models.DateTimeField('Last call')
    status = models.BooleanField('Status')
    
    def __str__(self):
        return self.full_name
    
    
    class Meta:
        
        verbose_name = "inactive client"
        verbose_name_plural= "inactive clients"


class ReplenishmentNotOlder(models.Model):
    # Creates a model in which there will be a list of clients who replenished the balance less than six months ago
    full_name = models.CharField('Full name', max_length=500)
    email = models.CharField('Email', max_length=500)
    address = models.CharField('Address', max_length=500)
    phone_number = models.CharField('Phone', max_length=500)
    current_balance = models.FloatField('Balance')
    last_payment = models.DateTimeField('Last payment')
    reg_date = models.DateTimeField('Data')
    lastcall_date = models.DateTimeField('Last call')
    status = models.BooleanField('Status')
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "replenishment not older"
        verbose_name_plural= "replenishment not olders"
      
      
class CallOlder(models.Model):
    # Creates a model in which there will be a list of clients who called more than six months ago
    full_name = models.CharField('Full name', max_length=500)
    email = models.CharField('Email', max_length=500)
    address = models.CharField('Address', max_length=500)
    phone_number = models.CharField('Phone', max_length=500)
    current_balance = models.FloatField('Balance')
    last_payment = models.DateTimeField('Last payment')
    reg_date = models.DateTimeField('Data')
    lastcall_date = models.DateTimeField('Last call')
    status = models.BooleanField('Status')
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "call older"
        verbose_name_plural= "call olders"
        
        
class ErrorClients(models.Model):
    # Creates a model in which there will be a list of false clients
    full_name = models.CharField('Full name', max_length=500)
    email = models.CharField('Email', max_length=500)
    address = models.CharField('Address', max_length=500)
    phone_number = models.CharField('Phone', max_length=500)
    current_balance = models.FloatField('Balance')
    last_payment = models.DateTimeField('Last payment')
    reg_date = models.DateTimeField('Data')
    lastcall_date = models.DateTimeField('Last call')
    status = models.BooleanField('Status')
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "error client"
        verbose_name_plural= "error clients"
