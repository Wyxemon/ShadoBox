import string
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
    print("2. OSINT: encontrar usuarios con Sherlock (solo para Linux)")
    print("3. HACKING WIFI con wifite (WPS, WPA, WPA2, handshake...)")
    print("4. Salir")

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
        print("Saliendo del programa... ¡Hasta luego! 😊")
        break

    elif user in ["1", "generar contraseña"]:
        contraseña = generar_contraseña()
        print(f"Contraseña segura generada: {contraseña}")

    elif user in ["2", "menu"]:
        if not os.path.exists("sherlock/sherlock.py"):
            print("\n[!] Sherlock no está instalado, instalando...\n")
            subprocess.run(("sudo", "apt", "install", "git"))
            subprocess.run(["git", "clone", "https://github.com/sherlock-project/sherlock"])
            subprocess.run(["pip", "install", "-r", "sherlock/requirements.txt"])
        else:
            print("[+] Sherlock ya está instalado")

        os.system('clear')
        username = input("\n[+] Target username: ")
        subprocess.run(["sherlock", username])
    elif user in ["3", "menu"]:
        if not os.path.exists("/usr/bin/wifite"):
            print("\n[!] Wifte no esta instalado, instalando...")
            subprocess.run(("sudo", "apt", "install", "wifite"))
            os.system('clear')
            os.system('sudo su')
            subprocess.run(("wifite"))

    else:
        print("Opción no reconocida. Escribe 'menu' para ver las opciones.")
                                                                                                                                                                                           31,16         Bot

                                                                                                                           
                                                                                                                                                                                                            

                                                                                                                                                                                                                                                                                                                                                                  8,49          All
                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                                                                                                                   56,82-81      All
