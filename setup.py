import os

os.system("pip3 install colored")
os.system("pip3 install pyautogui")
os.system("pip3 install selenium")
os.system("pip3 install python3")

import time
from termcolor import colored

success="""
|__________installation successful____________|
 =============================================
"""

can="""
|__________installation Cancelled____________|
 =============================================
"""

logo= """"
 ██▓ ███▄    █   ██████ ▄▄▄█████▓ ▄▄▄            ▄▄▄▄    ▄▄▄       ███▄    █ 
▓██▒ ██ ▀█   █ ▒██    ▒ ▓  ██▒ ▓▒▒████▄         ▓█████▄ ▒████▄     ██ ▀█   █ 
▒██▒▓██  ▀█ ██▒░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄       ▒██▒ ▄██▒██  ▀█▄  ▓██  ▀█ ██▒
░██░▓██▒  ▐▌██▒  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██      ▒██░█▀  ░██▄▄▄▄██ ▓██▒  ▐▌██▒
░██░▒██░   ▓██░▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒ ██▓ ░▓█  ▀█▓ ▓█   ▓██▒▒██░   ▓██░
░▓  ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░ ▒▓▒ ░▒▓███▀▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
 ▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░    ░      ▒   ▒▒ ░ ░▒  ▒░▒   ░   ▒   ▒▒ ░░ ░░   ░ ▒░
 ▒ ░   ░   ░ ░ ░  ░  ░    ░        ░   ▒    ░    ░    ░   ░   ▒      ░   ░ ░ 
 ░           ░       ░                 ░  ░  ░   ░            ░  ░         ░ 
                                             ░        ░                  [v1.0]  
"""


about1="""
[-]This tool is Created By Cyber-D team(K.D.O)
"""

about2="""
Author    :  K.D.O [ Cyber-D Team ]
Github    :  https://github.com/kdo2064
instagram :  https://instagram.com/kdo_shashank
Version   :  1.1
"""

about3="""
 Warning:
"""

about4="""  
This Tool is made for educational purpose
only ! Owner will not be responsible for
any misuse of this tool !
"""
social_media= """
 ~ Instagram: https://instagram.com/kdo_shashank
 ~ Whatsapp: https://wa.me/+9779746554757
 ~ Telegram: https://t.me/kdobhai
 ~ Cyber.Arpan: https://www.instagram.com/cyber.arpan
"""

def installer():
    os.system("clear")
    print(colored(logo,"red"))
    print(colored(about1,"green",attrs=['reverse', 'blink']) + (colored(about2,"yellow")) + (colored(about3,"red",attrs=['reverse', 'blink'])) + colored(about4,"blue") )
    install = input(colored("Do you want to install Insta.Ban[y/n]:","yellow"))
    if install == "y":
        os.system("cd /home && rm -rf instaban")
        os.system("git clone https://github.com/kdo2006/instaban")
        print(colored(success,"red"))
        os.system("cd instaban && python3 instaban.py")
    elif install == "n":
        print(colored(can,"red"))
    else:
        print(colored("invailed options...!","red"))
        time.sleep(2)
        installer()

if __name__=="__main__":
    installer()