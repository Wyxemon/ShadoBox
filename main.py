#!/usr/bin/env python3

import subprocess
import os
import secrets
import string

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
    print("1. Generar contraseña segura")
    print("2. OSINT: encontrar usuarios con sherlock (solo para linux)")
    print("3. Salir")

def generar_contraseña(longitud=16):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contraseña

# Mostrar el menú al inicio
print(menu_icon)
menu()

while True:
    user = input("\nUser > ").strip().lower()  # Limpia espacios y normaliza entrada

    match user:
        case "exit" | "3":
            print("Saliendo del programa... ¡Hasta luego! 😊")
            break

        case "menu" | "2":
            if not os.path.exists("sherlock/sherlock.py"):
                print("Sherlock is not installed, instaling...")
                subprocess.run[("git", "clone", "https://github.com/sherlock-project/sherlock")]
                subprocess.run[("pip", "install" "-r" "/sherlock/requirements.txt")]
            else:
                print("[+] Sherlock is already installed")
           os.system('clear')
           username = input("Target username: ")
            subprocess.run[("sherlock", username)]

        case "generar contraseña" | "1":
            contraseña = generar_contraseña()
            print(f"Contraseña segura generada: {contraseña}")

        case _:
            print("Opción no reconocida. Escribe 'menu' para ver las opciones.")
                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                                                                                                                   56,82-81      All
