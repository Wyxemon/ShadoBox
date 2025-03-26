#!/usr/bin/env python3

import os
import shutil
from subprocess import run, CalledProcessError, DEVNULL
from password import generar_contraseña
from osint import HoleHe
from nmap import nmap, menu, menu_python, menu_linux
# import nmap

_menu_icon = """\n
   ██████  ██░ ██  ▄▄▄      ▓█████▄  ▒█████   ▄▄▄▄    ▒█████  ▒██   ██▒
▒██    ▒ ▓██░ ██▒▒████▄    ▒██▀ ██▌▒██▒  ██▒▓█████▄ ▒██▒  ██▒▒▒ █ █ ▒░
░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ░██   █▌▒██░  ██▒▒██▒ ▄██▒██░  ██▒░░  █   ░
  ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ░▓█▄   ▌▒██   ██░▒██░█▀  ▒██   ██░ ░ █ █ ▒ 
▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒░▒████▓ ░ ████▓▒░░▓█  ▀█▓░ ████▓▒░▒██▒ ▒██▒
▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░▒░▒░ ░▒▓███▀▒░ ▒░▒░▒░ ▒▒ ░ ░▓ ░
░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░ ░ ▒  ▒   ░ ▒ ▒░ ▒░▒   ░   ░ ▒ ▒░ ░░   ░▒ ░
░  ░  ░   ░  ░░ ░  ░   ▒    ░ ░  ░ ░ ░ ░ ▒   ░    ░ ░ ░ ░ ▒   ░    ░  
      ░   ░  ░  ░      ░  ░   ░        ░ ░   ░          ░ ░   ░    ░  
                            ░                     ░                   

                
"""

# * FUNCIONES

def menu():
    print("\n--- MENÚ ---")
    print("1. GENERATE SAFE PASSWORD")
    print("2. OSINT: SEARCH USERNAMES WITH SHERLOCK")
    print("3. HACKING WIFI PASSWORD WITH WIFITE WPS, WPA, WPA2, handshake... ([!] Warning you need a wifi adapter)")
    print("4. PORT SCANNER")
    print("5. HELP")
    print("6. EXIT")
    



def nmap():
    try:
        if shutil.which("nmap"):
            print("You have nmap in your system")
            menu()

    except CalledProcessError:
        one = input("You don't have nmap installed. Do you want to update your system before the installation? (Y/n): ")

        if one.lower() in ["y", "yes"]:
                try:
                    run("sudo", "apt", "update", check=True)
                    run("sudo", "apt", "upgrade", check=True)
                
                except CalledProcessError:
                    print("This user isn't in the sudoers list, use other user with Super User permissions")
                    return
                
        else:
                print("Skipping system update...")

        try:
            
            print("Installing nmap...\n")
            run("sudo", "apt", "install", "nmap", check=True)
            print("Nmap is installed in your system now.")
            menu()
            
        except CalledProcessError:
                print("This user isn't in the sudoers list, use other user with Super User permissions")
        
                
    def menu():
        os.system("clear")
        print("""\n
███╗░░██╗███╗░░░███╗░█████╗░██████╗░
████╗░██║████╗░████║██╔══██╗██╔══██╗
██╔██╗██║██╔████╔██║███████║██████╔╝
██║╚████║██║╚██╔╝██║██╔══██║██╔═══╝░
██║░╚███║██║░╚═╝░██║██║░░██║██║░░░░░
╚═╝░░╚══╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░

1. Python NMAP
2. Linux NMAP
3. Help
4. Return to menu""")
        
        two = input("\nUser (nmap) > ")
        
        if two.lower() in ["1", "python nmap"]:
            menu_python()
        
        elif two.lower() in ["2", "linux nmap"]:
            menu_linux()
            
        elif two.lower() in ["3", "help"]:
            print("""
Python NMAP: Using the nmap library
Linux NMAP: Using the NMAP of your PATH""")
        
        if two.lower() in ["4", "return"]:
            return
        
        
    def menu_python():
        os.system("clear")
        print("""\n

--TYPES OF SCANS--
1. Simple Scan
2. Complete Scan
3. Quiet Scan (no ping)
4. OS and Traceroute Detection Scan
5. Service Version Detection Scan
6. Leave NMAP And Return To Menu""")
    
        three = input("\nUser (nmap --> Python-nmap) > ")
    
        if three.lower() in ["1", "simple scan"]:
            host = input("\nPut here the IP of the domain or host to scan: 1")
    
        elif three.lower() in ["2", "complete scan"]:
            host = input("\nPut here the IP of the domain or host to scan: 2")
    
        elif three.lower() in ["3", "quiet scan"]:
            host = input("\nPut here the IP of the domain or host to scan: 3")
    
        elif three.lower() in ["4", "os"]:
            host = input("\nPut here the IP of the domain or host to scan: 4")
    
        elif three.lower() in ["5", "service"]:
            host = input("\nPut here the IP of the domain or host to scan: 5")
        
        elif three.lower() in ["6", "leave"]:
            return menu
    
        elif three.lower() in ["menu"]:
            menu_python()
    
        else:
            print("Unrecognized option. Type 'menu' to see the options.")
        
        
    def menu_linux():
        put_linux = "nmap function" #seguir aqui2
        

def pip():
    try:
        run(("pip", "--version"), check=True)
        print("You have pip in your system")
        
    except CalledProcessError:
        one = input("You don't have pip installed. Do you want to update your system before the installation? (Y/n): ")

        if one.lower() in ["y", "yes"]:
            run(("sudo", "apt", "update"))
            run(("sudo", "apt", "upgrade"))
            
        else:
            print("Skipping system update...")

        run(("sudo", "apt", "install", "pip"))
        print("Installing pip...\n")
        print("Pip is installed in your system now.")

# * USUARIO

# Mostrar el menú al inicio
print(_menu_icon)
menu()

while True:
    user = input("\nUser > ").strip().lower()  # Limpia espacios y normaliza entrada

    if user in ["exit", "6"]:
        print("Leaving the program... ¡Goodbye! 😊")
        break

    elif user in ["1", "generar contraseña"]:
        contraseña = generar_contraseña()
        print(f"Safe password created: {contraseña}")

    elif user in ["2", "Sherlok"]:
        if not os.path.exists("sherlock/sherlock.py"):
            print("\n[!] Sherlock is not installed, installing...\n")
            run(("sudo", "apt", "update"))
            run(("sudo", "apt", "install", "sherlock"))
        else:
            print("[+] Sherlock is already installed")

        os.system('clear')
        username = input("\n[+] Target username: ")
        run(["sherlock", username])
        
    elif user in ["3", "Wifite"]:
        if not os.path.exists("/usr/bin/wifite"):
            print("\n[!] Wifte is not installed, installing...")
            run(("sudo", "apt", "install", "wifite"))
            os.system('clear')
            print("\n[-] YOU NEED A WIFI ADAPTOR WITH MONITOR OPTION AND INSTALL SOME DEPNDENCE")
            run(("sudo", "apt", "install", "hcxdumptool"))
            run(("sudo", "apt", "install", "hcxtools"))
            run(("sudo", "apt", "install", "aircrack-ng"))
            run(("sudo", "apt", "install", "bully"))
            os.system("sleep 5")
            run(("sudo", "wifite"))
    
    elif user in ["4", "nmap"]:
        nmap()

    elif user in ["menu"]:
        menu()

    elif user in ["clear", "cls"]:
        run("cls" if os.name == "nt" else "clear", shell=True)
        print(_menu_icon)

    else:
        print("Unrecognized option. Type 'menu' to see the options.")