from datetime import datetime
from datetime import date
from time import sleep
import os , requests , json , csv
from typing import Awaitable

def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
today = date.today()
now = datetime.now()
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
\n\n\n\n
      
Author: Geeky Faahad


Its just a coffee bot
""")
#sleep(0.5)
name = input("What is your name?\n")
clear()
#sleep(0.7)
print("Hello "+ name[0].upper() +""+ name[1:] +"!\n\n\n")
print("What would you like from our menu today? \nHere is what we are serving.\n", end="\r")
menu = input("Black Coffee , Expresso , Cappacuino , Cold Brew\n")
clear()
print("You choose "+ menu +" Great Choice 👍\n")
order = input("How many cups of coffee?\n")
clear()
print("Your order "+ menu +" and "+ order +" cups of coffee\n")
#sleep(1)
#print("Please wait\n")
#sleep(1.5)
#print("Please wait while we are making up your total\n\n")
#sleep(2)
total=int(order) * 50
print("Your Total is Rs." +str(total)) 
payload = {"TIME" : str(now),"Name" : name,"MENU" : menu,"QUANTITY" : order,"TOTAL" : total,}
json_object = json.dumps(payload, indent = 6)
with open('data.json', 'a' ) as outfile:
    outfile.write(""+json_object+"\n")
r = requests.post('Enter_Your_Api_Link_Here', json=payload)
