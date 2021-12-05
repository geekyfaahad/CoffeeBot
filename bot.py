from datetime import datetime
from datetime import date
from time import sleep
import os,requests,json,socket
from typing import Awaitable
from dhooks import Webhook
import pyfiglet


#############  Functions   ################
result = pyfiglet.figlet_format("C o f f e e H u B", font = "5lineoblique" )
nointernet = pyfiglet.figlet_format("No Internet", font = "banner" )
hook = Webhook('https://discord.com/api/webhooks/917066155548618852/WeTxA_SHcUr2VOZhUjefQUzx7LyVzwT14nhi5Xga5Pk-lmsrUPA2-44rqvomO2mneH8a')
today = date.today()
now = datetime.now()
lines  = ("-" * 40)
print(str(lines))
ip = socket.gethostbyname(socket.gethostname())
def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
clear()
# def exit():
# 	if os.name == 'nt':
# 		os.system('exit')
# 	else:
# 		os.system('exit')
if ip=="127.0.0.1":
    print(nointernet)
    print("Please Connect to Internet")
    exit()
else:
    print("Connected, with the IP address: "+ ip )

#############  Functions   ################

   
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
Author: Geeky Faahad , Aaqib Ahmad

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
print("You choose "+ menu.upper() +" Great Choice 👍\n")
order = input("How many cups of "+ menu.upper() +"\n")
clear()
print("Your order "+ menu.upper() +"\n"+ order.upper() +" cups\n")
# sleep(1)
# print("Please wait\n")
# sleep(1.5)
# print("Please wait while we are making up your total\n\n")
if menu.upper().endswith('BLACK COFFEE'):
                price=50
elif menu.upper().endswith('EXPRESSO'):
                price=80
elif menu.upper().endswith('CAPPACUINO'):
                price=120
elif menu.upper().endswith('COLD BREW'):
                price=100
else:
  print("not a valid menu option")
  exit()
if print=="not a valid menu option":
  exit()
# sleep(2)
total=int(order) * 50
print("Your Total is Rs " +str(total)) 
payload = {"TIME" : str(now),"Name" : name,"MENU" : menu,"QUANTITY" : order,"TOTAL" : total,}
json_object = json.dumps(payload, indent = 6)
with open('data.json', 'a' ) as outfile:
    outfile.write(""+json_object+"\n")
#WEBHOOK data
hook.send(f" {lines} \nIp Addresss: {ip}\nTime: {now}\nName: {name}\nMenu: {menu}\nOrder: {order}\nTotal: {total}\n{lines}")
r = requests.post('https://discohook.org/?data=eyJtZXNzYWdlcyI6W3siZGF0YSI6eyJjb250ZW50IjoiaGVsbG8iLCJlbWJlZHMiOm51bGx9fV19', json=payload)
# p = input("do you want another coffee? Press Y Press N").lower()
# if p == 'y':
# elif p == 'n':
# exit()
# else:
# print("invalid query")
# main()
