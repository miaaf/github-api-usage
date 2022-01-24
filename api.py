#by github.com/miaaf

from asyncio.windows_events import NULL
from email.mime import base
from lib2to3.pgen2 import token
from types import NoneType
from urllib import response
from aiohttp import request
import pprint
import requests
import requests as r
import json
import base64
#from dotenv import load_dotenv
import os

#load_dotenv()

p = pprint.PrettyPrinter()

token = "YOUR ACCESS TOKEN" #https://github.com/settings/tokens

def get_followers(username):

    followers_list = f"https://api.github.com/users/{username}/followers"
    response = requests.get(followers_list, headers={"Authorization":"token {}".format(token)})
    data = response.json()

    print("\n\nFollowers: ")

    for i in range(0, len(data)):
        follower_name = data[i]["login"]
        print(follower_name)  
        i += 1

def get_following(username):

    following_list = f"https://api.github.com/users/{username}/following"
    response = requests.get(following_list, headers={"Authorization":"token {}".format(token)})
    data = response.json()

    print("\n\nFollowing: ")

    for i in range(0, len(data)):
        following_name = data[i]["login"]
        print(following_name)  
        i += 1

def get_repos(username):

    repos_list = f"https://api.github.com/users/{username}/repos"
    response = requests.get(repos_list, headers={"Authorization":"token {}".format(token)})
    data = response.json()

    print("\n\nAll Repositories: ")

    for i in range(0, len(data)):
        repos_name = data[i]["svn_url"]
        print(repos_name)  
        print("Info of the project: Language : " + str(data[i]["language"]) +" Stars : " + str(data[i]["stargazers_count"]) + " Watchers : " + str(data[i]["watchers_count"]))  
        if data[i]["license"]:  
            print("License: " + data[i]["license"]["name"])  
        else:  
            print("That repository has no license!")  
        i += 1

def get_subs(username):

    subscriptions_list = f"https://api.github.com/users/{username}/subscriptions"
    response = requests.get(subscriptions_list, headers={"Authorization":"token {}".format(token)})
    data = response.json()

    print("\n\nAll Subscriptions: ")

    for i in range(0, len(data)):
        subs_name = data[i]["svn_url"]
        print(subs_name + " by " + data[i]["owner"]["login"])  
        print("Info of the project: Language : " + str(data[i]["language"]) +" Stars : " + str(data[i]["stargazers_count"]) + " Watchers : " + str(data[i]["watchers_count"]))  
        if data[i]["license"]:  
            print("License: " + data[i]["license"]["name"])  
        else:  
            print("That repository has no license!")  
        i += 1

def get_starred_list(username):

    starred_list = f"https://api.github.com/users/{username}/starred"
    response = requests.get(starred_list, headers={"Authorization":"token {}".format(token)})
    data = response.json()

    print("\n\nAll Starred Repositories: ")

    for i in range(0, len(data)):
        starred_name = data[i]["svn_url"]
        print(starred_name + " by " + data[i]["owner"]["login"])  
        print("Info of the project: Language : " + str(data[i]["language"]) +" Stars : " + str(data[i]["stargazers_count"]) + " Watchers : " + str(data[i]["watchers_count"]))  
        if data[i]["license"]:  
            print("License: " + data[i]["license"]["name"])  
        else:   
            print("That repository has no license!")  
        i += 1

def get_info(username):

    base_url = f"https://api.github.com/users/{username}"

    r = requests.get(base_url, headers={"Authorization":"token {}".format(token)})
    data = r.json()

    login_name = data["login"]

    name = data["name"]

    bio = data["bio"]

    type = data["type"]

    site_admin = data["site_admin"]

    id = data["id"]

    node_id = data["node_id"]

    avatar_url = data["avatar_url"]

    gravatar_id = data["gravatar_id"]

    url = data["url"]

    html_url = data["html_url"]

    company = data["company"]

    location = data["location"]

    public_repos = data["public_repos"]

    follower_count = data["followers"]

    following_count = data["following"]

    created_at = data["created_at"]

    last_update = data["updated_at"]

    two_factor = data["two_factor_authentication"]

    print("Login name: " + login_name)

    print("Name: " + name)

    print("Created at: " + created_at)

    print("Last update at: " + last_update)

    print("HTML URL: " + html_url)

    print("URL: " + url)

    print("ID: " + str(id))

    print("Node ID: " + str(node_id))

    print("Gravatar ID: " + str(gravatar_id))

    if bio:
        print("Bio: " + bio)
    else:
        print("Bio: null")

    print("Type: " + type)

    print("Avatar URL: " + avatar_url)
    
    print("Company: " + company)

    print("Location: " + location)

    print("Site Admin: " + str(site_admin))

    print("Public Repositories Count: " + str(public_repos))

    print("Follower Count: " + str(follower_count))

    print("Following Count: " + str(following_count))

    print("Two Factor: " + str(two_factor))

    get_followers(username)

    get_following(username)

    get_repos(username)

    get_subs(username)

    get_starred_list(username)



username = input("Enter the username that you want to get info: ")

get_info(username)