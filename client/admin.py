from django.contrib import admin
from .models import ClientsList, InactiveClients, ReplenishmentNotOlder,  CallOlder, ErrorClients 

# Adds all specified models to the admin

class ClientsListAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'address', 'phone_number', 'current_balance', 'status')
    
    
class InactiveClientsAdmin(admin.ModelAdmin):
    list_inactiveclientsadmin = ('full_name', 'email', 'address', 'phone_number', 'current_balance', 'status')
   
    
class ReplenishmentNotOlderAdmin(admin.ModelAdmin):
    list_replenishmentnotolder = ('full_name', 'email', 'address', 'phone_number', 'current_balance', 'status')
   
    
class CallOlderAdmin(admin.ModelAdmin):
    list_callolder = ('full_name', 'email', 'address', 'phone_number', 'current_balance', 'status')
    
    
class ErrorClientsAdmin(admin.ModelAdmin):
    list_error = ('full_name', 'email', 'address', 'phone_number', 'current_balance', 'status')
  
    
admin.site.register(ClientsList, ClientsListAdmin)
admin.site.register(InactiveClients, InactiveClientsAdmin)
admin.site.register(ReplenishmentNotOlder, ReplenishmentNotOlderAdmin)
admin.site.register(CallOlder, CallOlderAdmin)
admin.site.register(ErrorClients, ErrorClientsAdmin)
