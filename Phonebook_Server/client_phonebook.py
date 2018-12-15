#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 00:20:47 2018

@author: hannaholdorf
"""

#%%

import requests

def add_contact(name,phone):
    
    response = requests.post("http://127.0.0.1:5000/add_contact/" + name + "/" + phone).json()
    
    return response

add_contact("Anikken","730098")

#%%

def lookup_number(name):
    
    response = requests.get("http://127.0.0.1:5000/lookup_number/" + name).json()
    
    return response

lookup_number("Thibault")

#%%

def delete_contact(name):
    
    response = requests.delete("http://127.0.0.1:5000/delete_contact/" + name).json()
    
    return response

delete_contact("Leila")

#%%

def update_number(name,phone):
    
    response = requests.get("http://127.0.0.1:5000/update_number/" + name + "/" + phone).json()
    
    return response

update_number("Natalie","7654339")