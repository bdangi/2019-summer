#!/usr/bin/env python3

import os
import sqlite3
import json

data_path = os.path.expanduser('~')+"/.mozilla/firefox/5nsm941v.default"

files = os.listdir(data_path)

history_db = os.path.join(data_path, 'places.sqlite')

c = sqlite3.connect(history_db)

cursor = c.cursor()

select_statement = "select moz_places.url, moz_places.visit_count from moz_places;"

select_all = "select * from moz_places;"

# execute the query to get the data...
cursor.execute(select_statement)

results = cursor.fetchall()

# get and print the data
print("Now printing the browser history data...")
print(" ")
for url, count in results:
 print("Url")
 print(url)
 print("Count")
 print(count)
 print(" ")

cursor.execute(select_all)
results_all = cursor.fetchall()
print(" ")
print("Printing all results from the history: ")
print(" ")
for res in results_all:
 print(res)
 print(" ")

# open the json file that contains login credentials information
with open('/home/ram/.mozilla/firefox/5nsm941v.default/logins.json') as json_file:
     data = json.load(json_file)
# print everything from login file
     print(" ")
     print(" ")
     print("Printing logins.json file...")
     print(" ")
     for string in data['logins']:
         print(string)

# print only url, username and password
     print(" ")
     print(" ")
     print("Now print the data")
     print(" ")
     for login in data['logins']:
         print('Hostname: ' + login['hostname'])
         print(" ")
         print('Encrypted Username: ' + login['encryptedUsername'])
         print(" ")
         print('Encrypted Password: ' + login['encryptedPassword'])
         print(" ")
