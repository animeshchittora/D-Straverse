#!/usr/bin/env python
import requests

print("Welcome to Web crawler")
print("press 1 for subdomains traversal 2 for directory traversal")

number = input("Enter your choice :   ")
if(number==1):
    def request(url):
        try:
            return  requests.get("http://"+url)
        except requests.exceptions.ConnectionError:
            pass
    target_url = raw_input("Enter your URL: ---->   ")

    with open("/home/ani/Downloads/subdomains-wodlist.txt","r") as wordlist_file: #Subdomain_list-Path
        for line in wordlist_file:
            word = line.strip()
            test_url = word+"."+target_url
            response = request(test_url)
            if response:
                print("[+] Discovered Domains ---->> "+test_url)
elif(number==2):
    def request(url):
        try:
            return  requests.get("http://"+url)
        except requests.exceptions.ConnectionError:
            pass
    target_url = raw_input("Enter your URL: ---->   ")
    with open("/home/ani/Downloads/files-and-dirs-wordlist.txt","r") as wordlist_file:  #Directory_list-path
        for line in wordlist_file:
            word = line.strip()
            test_url = target_url+"/"+word
            response = request(test_url)
            if response:
                print("[+] Discovered Domains ---->> "+test_url)
