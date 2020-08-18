import fbchat
from fbchat import Client
from getpass import getpass
import requests

url = "https://www.fast2sms.com/dev/bulk"

querystring = {"authorization":"Ryc5XuMIzOAtLUke6Y40w3TNp8QVCa1jxWslg7hZKnmodGP9bvvNtYh2PAE7O09IfHjwJZXgMius5R6q","sender_id":"FSTSMS","message":"this is a test message","language":"english","route":"p","numbers":"7026113916"}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

print(""" .......................................................
				WELCOME  
....................................................... """)
username="7026113745"
client=fbchat.Client(username,getpass())
no_of_friends=int(input("Number of friends:"))
for i in range(no_of_friends):
    name=str(input("Name:  "))
    friends=client.searchForUsers(name)
    friend=friends[0]
    msg=str(input("Message: "))
    sent=client.send(fbchat.models.Message(msg),friend.uid)
    if sent:
        print("message sent successfully")