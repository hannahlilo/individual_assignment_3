#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 19:04:18 2018

@author: hannaholdorf
"""

#%%

from flask import Flask, jsonify

server = Flask("phonebookserver")

phonebook = {"Leila":"9376822","Thibault":"0338769","Natalie":"2776357"}

@server.route("/add_contact/<name>/<phone>", methods = ["POST"])
def add_contact(name,phone): 
    phonebook[name] = phone   
    return jsonify(name + " is added to your list of contacts")

@server.route("/lookup_number/<name>")
def lookup_number(name): 
    phone = phonebook[name]   
    return jsonify(name + "'s phone number is " + phone)

@server.route("/delete_contact/<name>", methods = ["DELETE"])
def delete_contact(name): 
    if name in phonebook:
        phonebook.remove(name)
        return jsonify("Contact not in phonebook")

@server.route("/update_number/<name>/<phone>")
def update_number(name,phone): 
    phonebook[name] = phone   
    return jsonify(name + " updated to " + phone)

@server.route("/phonebook")
def show_phonebook():
    return jsonify(phonebook)


server.run()
