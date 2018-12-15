#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 18:12:27 2018

@author: hannaholdorf
"""



#%% Using Github’s API, create a function that takes all repositories from your account

def list_repos(username):
    
    import requests
       
    json_data = requests.get("https://api.github.com/users/" + username + "/repos").json()

    for repo in json_data:
        print("name: " + repo["name"])


list_repos("hannahlilo")      
    

#%% Using Github’s API, create a function that prints a 
# short description of each repository, with its name, number of stars, main language, and url
    
def info_repos(username):
    
    import requests

    json_data = requests.get("https://api.github.com/users/" + username + "/repos").json()

    for repo in json_data:
        print("Name: " + repo["name"], 
              "Url: " + repo["html_url"],
              "Language: " + str(repo["language"]), 
              "Stars: " + str(repo["stargazers_count"]),
              "Description: " + str(repo["description"]))
        

info_repos("hannahlilo")
