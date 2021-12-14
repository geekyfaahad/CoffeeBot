from datetime import datetime
from datetime import date
from time import sleep
import os, requests, json, socket, sys
from typing import Awaitable
from dhooks import Webhook
import pyfiglet

#############  Functions   ################
result = pyfiglet.figlet_format("C o f f e e  H u B", font="big")
nointernet = pyfiglet.figlet_format("No Internet", font="banner")
# hook = Webhook('Enter_Discord_Api_Key')
# base_url = "Enter_Telegram_Api_KEY"
today = date.today()
now = datetime.now()
lines = "-" * 40
print(str(lines))
ip = socket.gethostbyname(socket.gethostname())


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


clear()
# def exit():
# 	if os.name == 'nt':
# 		os.system('exit')
# 	else:
# 		os.system('exit')
if ip == "127.0.0.1":
    print(nointernet)
    print("Please Connect to Internet")
    exit()
else:
    print("Connected, with the IP address: " + ip)

#############  Functions   ################

while True:
    print(now)
    print(result)
    print(
        """
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
        """
    )

    # sleep(0.5)
    name = input("What is your name?\n")
    clear()
    # sleep(0.7)
    print("Hello " + name[0].upper() + "" + name[1:] + "!\n\n\n")
    print(
        "What would you like from our menu today? \nHere is what we are serving.\n",
        end="\r",
    )
    menu = input("Black Coffee , Expresso , Cappacuino , Cold Brew\n")
    if menu.upper().endswith("BLACK COFFEE"):
        price = 50
    elif menu.upper().endswith("EXPRESSO"):
        price = 80
    elif menu.upper().endswith("CAPPACUINO"):
        price = 120
    elif menu.upper().endswith("COLD BREW"):
        price = 100
    else:
        print("not a valid menu option")
        exit()
    clear()
    print("You choose " + menu.upper() + " Great Choice 👍\n")
    order = input("How many cups of " + menu.upper() + "\n")
    clear()
    print("Your order " + menu.upper() + "\n" + order.upper() + " cups\n")
    # sleep(1)
    # print("Please wait\n")
    # sleep(1.5)
    # print("Please wait while we are making up your total\n\n")
    # sleep(2)
    total = int(order) * price
    print("Your Total is Rs " + str(total))
    # payload = {"TIME" : str(now),"Name" : name,"MENU" : menu,"QUANTITY" : order,"TOTAL" : total,}
    # json_object = json.dumps(payload, indent = 6)
    # with open('data.json', 'a' ) as outfile:
    #     outfile.write(""+json_object+"\n")
    # r = requests.post('Enter_Api_Key', json=payload)

    # WEBHOOK data
    # hook.send(f" {lines} \nTime: {now}\nIp Addresss: {ip}\nName: {name.upper()}\nMenu: {menu.upper()}\nOrder: {order}\nTotal: {total}\n{lines}")
    # p = input("do you want another coffee? Press Y Press N").lower()

    # telegram data
    # parameters = {
    #     "chat_id" : "Enter_Chat_id",
    #     "text" : ("Time: "+str(now)+"\nIp Addresss: "+ip+"\nName: "+name.upper()+"\nMENU: "+menu.upper()+"\nQuantity: "+order+"\nTotal: "+str(total).upper()+"")
    # }
    # r = requests.get(base_url, data = parameters)
    # print(r.text)

    o = input("Do you want to repeat this program\nPress Yes(y)\nPress NO(n)\n")

    if o == "y":
        continue
    elif o == "n":
        exit()
    else:
        print("Invalid Entry")
        print("You are exiting get out")
        sleep(2)
        exit()
