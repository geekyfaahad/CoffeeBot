from datetime import datetime
from datetime import date
from time import sleep
import os
import requests
import json
import socket
from typing import Awaitable
from dhooks import Webhook
import pyfiglet
result = pyfiglet.figlet_format("C o f f e e H u B", font = "5lineoblique" )
hook = Webhook('https://discord.com/api/webhooks/917066155548618852/WeTxA_SHcUr2VOZhUjefQUzx7LyVzwT14nhi5Xga5Pk-lmsrUPA2-44rqvomO2mneH8a')
today = date.today()
now = datetime.now()
ip = socket.gethostbyname(socket.gethostname())
def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
clear()
print(now)
print("""
                       .
                        `:.
                          `:.
                  .:'     ,::
                 .:'      ;:'
                 ::      ;:'

                  :    .:'
                   `.  :.
          _________________________
         : _ _ _ _ _ _ _ _ _ _ _ _ :
     ,---:".".".".".".".".".".".".":
    : ,'"`::.:.:.:.:.:.:.:.:.:.:.::'
    `.`.  `:-===-===-===-===-===-:'
      `.`-._:                   :
        `-.__`.               ,' 
    ,--------`"`-------------'--------.
     `"--.__                   __.--"'
            `""-------------""'
\n\n
Author: Geeky Faahad

Its just a coffee bot
""")
# sleep(0.5)
name = input("What is your name?\n")
clear()
# sleep(0.7)
print("Hello "+ name[0].upper() +""+ name[1:] +"!\n\n\n")
print("What would you like from our menu today? \nHere is what we are serving.\n", end="\r")
menu = input("Black Coffee , Expresso , Cappacuino , Cold Brew\n")
clear()
print("You choose "+ menu +" Great Choice 👍\n")
order = input("How many cups of coffee?\n")
clear()
print("Your order "+ menu +"\n"+ order +" cups\n")
# sleep(1)
# print("Please wait\n")
# sleep(1.5)
# print("Please wait while we are making up your total\n\n")
# sleep(2)
total=int(order) * 50
print("Your Total is Rs " +str(total)) 
payload = {"TIME" : str(now),"Name" : name,"MENU" : menu,"QUANTITY" : order,"TOTAL" : total,}
json_object = json.dumps(payload, indent = 6)
with open('data.json', 'a' ) as outfile:
    outfile.write(""+json_object+"\n")
#WEBHOOK data
hook.send(f"---------------------\nIp Addresss: {ip}\nTime: {now}\nName: {name}\nMenu: {menu}\nOrder: {order}\nTotal: {total}\n---------------------")
r = requests.post('https://discohook.org/?data=eyJtZXNzYWdlcyI6W3siZGF0YSI6eyJjb250ZW50IjoiaGVsbG8iLCJlbWJlZHMiOm51bGx9fV19', json=payload)
# p = input("do you want another coffee? Press Y Press N").lower()
# if p == 'y':
# elif p == 'n':
# exit()
# else:
# print("invalid query")
# main()
