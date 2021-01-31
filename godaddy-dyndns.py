#!/usr/bin/python3
from godaddypy import Client, Account
import os
from os import path
from os import getenv
import requests
import time
import datetime
import sys

#Enable Logging
now = str(datetime.datetime.now()) + ' | '

#Confirm variables are set
try:
  subdomains = os.environ.get('SUBDOMAINS').split(';')
  domain = os.environ.get('DOMAIN')
  apiKey = os.environ.get('GODADDY_KEY')
  secret = os.environ.get('GODADDY_SECRET')
except:
  print(now+'One or more environment variables not set, exiting program.')
  sys.exit()

#Get current public IP
currentPublicIP = requests.get("https://api.ipify.org").text

#Check if cache file exists
if path.exists("/cache.txt"):
  print(now + 'Cached IP file exists, comparing current public IP')
  cacheFile = open('/cache.txt','r')
  cachedIP = cacheFile.read()
  if cachedIP == currentPublicIP:
    print(now+'Update not needed.')
  else:
    #Use GoDaddyPy to interact with GoDaddy API
    print(now+'Public IP has changed, updating now!')
    my_acct = Account(api_key=apiKey, api_secret=secret)
    client = Client(my_acct)
    for singledomain in subdomains:
      #Update all subdomains if current public IP not the same as cached
      time.sleep(1)
      client.update_record_ip(currentPublicIP, domain, singledomain, 'A')
    print(now+'Records updated!')
  cacheFile.close()

else:
  #First run, create cache.txt
  print(now+'Cached IP file does not exist, creating and storing current public IP')
  newCacheFile = open('/cache.txt', 'w')
  newCacheFile.write(currentPublicIP)
  newCacheFile.close()

  my_acct = Account(api_key=apiKey, api_secret=secret)
  client = Client(my_acct)
  for singledomain in subdomains:
    time.sleep(1)
    client.update_record_ip(currentPublicIP, domain, singledomain, 'A')
