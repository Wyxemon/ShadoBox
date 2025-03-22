import string
import os
import secrets
import string
import subprocess
import nmap

menu_icon = """\n
██╗░░██╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗░██████╗░░░░░░░████████╗░█████╗░░███i██╗░██╗░░░░░
██║░░██║██╔══██╗██╔══██╗██║░██╔╝██║████╗░██║██╔════╝░░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
███████║███████║██║░░╚═╝█████═╝░██║██╔██╗██║██║░░██╗░█████╗░░░██║░░░██║░░██║██║░░██║██║░░░░░
██╔══██║██╔══██║██║░░██╗██╔═██╗░██║██║╚████║██║░░╚██╗╚════╝░░░██║░░░██║░░██║██║░░██║██║░░░░░
██║░░██║██║░░██║╚█████╔╝██║░╚██╗██║██║░░███║╚██████╔╝░░░░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗
╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
"""

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
        subprocess.run(("python", "--version"), check=True)

    except:
        one = input("You don't have nmap installed. Do you want to update your system before the installation? (Y/n): ")

        if one.lower() in ["y", "yes"]:
            subprocess.run(("sudo", "apt", "update"))
            subprocess.run(("sudo", "apt", "upgrade"))
        else:
            print("Skipping system update...")

        subprocess.run(("sudo", "apt", "install", "nmap"))
        print("Installing nmap...\n")
        print("Nmap is installed in your system now.")
        
    try:
        subprocess.run(("pip", "--version"), check=True)

    except:
        one = input("You don't have pip installed. Do you want to update your system before the installation? (Y/n): ")

        if one.lower() in ["y", "yes"]:
            subprocess.run(("sudo", "apt", "update"))
            subprocess.run(("sudo", "apt", "upgrade"))
            
        else:
            print("Skipping system update...")

        subprocess.run(("sudo", "apt", "install", "pip"))
        print("Installing pip...\n")
        print("Pip is installed in your system now.")
        
# Mostrar el menú al inicio
print(menu_icon)
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
            subprocess.run(("sudo", "apt", "install", "git"))
            subprocess.run(["git", "clone", "https://github.com/sherlock-project/sherlock"])
            subprocess.run(["pip", "install", "-r", "sherlock/requirements.txt"])
        else:
            print("[+] Sherlock is already installed")

        os.system('clear')
        username = input("\n[+] Target username: ")
        subprocess.run(["sherlock", username])
        
    elif user in ["3", "Wifite"]:
        if not os.path.exists("/usr/bin/wifite"):
            print("\n[!] Wifte is not installed, installing...")
            subprocess.run(("sudo", "apt", "install", "wifite"))
            os.system('clear')
            os.system('sudo su')
            subprocess.run(("wifite"))
    
    elif user in ["4", "nmap"]:
        nmap()

    else:
        print("Unrecognized option. Type 'menu' to see the options.")