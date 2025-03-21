import string
import os
import secrets
import string
import subprocess

menu_icon = """
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
    print("4. EXIT")

def generar_contraseña(longitud=16):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contraseña

# Mostrar el menú al inicio
print(menu_icon)
menu()

while True:
    user = input("\nUser > ").strip().lower()  # Limpia espacios y normaliza entrada

    if user in ["exit", "4"]:
        print("Leaving the program... ¡Goodbye! 😊")
        break

    elif user in ["1", "generar contraseña"]:
        contraseña = generar_contraseña()
        print(f"Safe password created: {contraseña}")

    elif user in ["2", "menu"]:
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
    elif user in ["3", "menu"]:
        if not os.path.exists("/usr/bin/wifite"):
            print("\n[!] Wifte is not installed, installing...")
            subprocess.run(("sudo", "apt", "install", "wifite"))
            os.system('clear')
            os.system('sudo su')
            subprocess.run(("wifite"))

    else:
        print("Unrecognized option. Type 'menu' to see the options.")