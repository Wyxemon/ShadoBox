#!/usr/bin/env python3

import string
import os
import secrets
import string
from subprocess import run
# import nmap

_menu_icon = """\n
██╗░░██╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗░██████╗░░░░░░░████████╗░█████╗░░███i██╗░██╗░░░░░
██║░░██║██╔══██╗██╔══██╗██║░██╔╝██║████╗░██║██╔════╝░░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
███████║███████║██║░░╚═╝█████═╝░██║██╔██╗██║██║░░██╗░█████╗░░░██║░░░██║░░██║██║░░██║██║░░░░░
██╔══██║██╔══██║██║░░██╗██╔═██╗░██║██║╚████║██║░░╚██╗╚════╝░░░██║░░░██║░░██║██║░░██║██║░░░░░
██║░░██║██║░░██║╚█████╔╝██║░╚██╗██║██║░░███║╚██████╔╝░░░░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗
╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
"""

# * FUNCIONES

def menu():
    print("\n--- MENÚ ---")
    print("1. GENERATE SAFE PASSWORD")
    print("2. OSINT: SEARCH USERNAMES WITH SHERLOCK")
    print("3. HACKING WIFI PASSWORD WITH WIFITE WPS, WPA, WPA2, handshake... ([!] Warning you need a wifi adapter)")
    print("4. PORT SCANNER WITH NMAP")
    print("5. HELP")
    print("6. EXIT")

def generar_contraseña(longitud=16):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contraseña

def nmap():
    try:
        run(("python", "--version"), check=True)

    except:
        one = input("You don't have nmap installed. Do you want to update your system before the installation? (Y/n): ")

        if one.lower() in ["y", "yes"]:
            run(("sudo", "apt", "update"))
            run(("sudo", "apt", "upgrade"))
        else:
            print("Skipping system update...")

        run(("sudo", "apt", "install", "nmap"))
        print("Installing nmap...\n")
        print("Nmap is installed in your system now.")
        
    try:
        run(("pip", "--version"), check=True)

    except:
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

    elif user in ["clear"]:
        run("clear")

    else:
        print("Unrecognized option. Type 'menu' to see the options.")
