from distutils.command.install_egg_info import safe_version
import os, datetime
from telnetlib import STATUS
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pars.settings")

import django
django.setup()
from django.core.management.base import BaseCommand
from client.models import ClientsList, InactiveClients, ReplenishmentNotOlder, CallOlder, ErrorClients
import requests
import json


url = "https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=clients"
res = requests.get(url)
data = res.json()


def clientslist():
    # Parsim in the Clientlist model of all users from the site
    for i in range(len(data)):
        ClientsList.objects
        save_clients = ClientsList(full_name = data[i]['full_name'], email = data[i]['email'], address = data[i]['address'], phone_number = data[i]['phone_number'],
                               current_balance = data[i]['current_balance'], last_payment = data[i]['last_payment'], 
                               reg_date = data[i]['reg_date'], lastcall_date = data[i]['lastcall_date'], status = data[i]['status'])
        save_clients.save()
    
    
def inactiveclients():
    # We take the information we need from the Clientlist model and record it in another model
    for i in range(ClientsList.objects.count()):
        client_list = ClientsList.objects.get(id=(i+1))
        if client_list.status == 0 and client_list.current_balance < 0:
            inactive_client= InactiveClients(full_name = client_list.full_name, email = client_list.email, address = client_list.address, phone_number = client_list.phone_number,
                               current_balance = client_list.current_balance, last_payment = client_list.last_payment, 
                               reg_date = client_list.reg_date, lastcall_date = client_list.lastcall_date, status = client_list.status)
            inactive_client.save()


def replenishmentnotolder():
    # We take the information we need from the Clientlist model and record it in another model
    date_today = str(datetime.datetime.today())[:10]
    date_today = [int(date_today[:4]), int(date_today[5:7])]
 
    date_today[1] -= 6

    if date_today[1] <= 0:
        date_today[1] = 12 + date_today[1]
        date_today[0] -= 1

    for i in range(ClientsList.objects.count()):
        client_list = ClientsList.objects.get(id=(i+1))
        date = str(client_list.last_payment)[:10]
        date = [int(date[:4]), int(date[5:7])]
   
        if client_list.status != 0 and date >= date_today:
            replenishment_not_older= ReplenishmentNotOlder(full_name = client_list.full_name, email = client_list.email, address = client_list.address, phone_number = client_list.phone_number,
                                current_balance = client_list.current_balance, last_payment = client_list.last_payment, 
                                reg_date = client_list.reg_date, lastcall_date = client_list.lastcall_date, status = client_list.status)
            replenishment_not_older.save()
     
     
def callolder():
    # We take the information we need from the Clientlist model and record it in another model
    date_today = str(datetime.datetime.today())[:10]
    date_today = [int(date_today[:4]), int(date_today[5:7])]
    date_today[1] -= 6
    if date_today[1] <= 0:
        date_today[1] = 12 + date_today[1]
        date_today[0] -= 1
        
    for i in range(ClientsList.objects.count()):
        client_list = ClientsList.objects.get(id=(i+1))
        date = str(client_list.lastcall_date)[:10]
        date = [int(date[:4]), int(date[5:7])]
        
        if client_list.status != 0 and date >= date_today:
            call_older = CallOlder(full_name = client_list.full_name, email = client_list.email, address = client_list.address, phone_number = client_list.phone_number,
                               current_balance = client_list.current_balance, last_payment = client_list.last_payment, 
                               reg_date = client_list.reg_date, lastcall_date = client_list.lastcall_date, status = client_list.status)
            call_older.save()
            
            
def errorclients():
    # We take the information we need from the Clientlist model and record it in another model
    for i in range(ClientsList.objects.count()):
        client_list = ClientsList.objects.get(id=(i+1))
        if client_list.status == 0 and client_list.current_balance > 0:
            error_clients= ErrorClients(full_name = client_list.full_name, email = client_list.email, address = client_list.address, phone_number = client_list.phone_number,
                               current_balance = client_list.current_balance, last_payment = client_list.last_payment, 
                               reg_date = client_list.reg_date, lastcall_date = client_list.lastcall_date, status = client_list.status)
            error_clients.save()
