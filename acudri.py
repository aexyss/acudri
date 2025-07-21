#!/usr/bin/env python3

import subprocess

#ejecutar lspci y capturar el resultado
##aqui avisa al usuario que se esta analizando
print("analizando hardware...")
##aqui dice que lscpi es una variable que usa subprocess y revisa el output
lspci =subprocess.check_output(["lspci"]).decode()
# Divide la salida en líneas
lines = lspci.splitlines()
# Crea un diccionario para almacenar la información de los dispositivos
devices = {}
# Itera sobre las líneas y extrae la información relevante
for line in lines:
       # Busca la cadena "VGA" o "3D" para identificar dispositivos gráficos
    if "VGA" in line or "3D" in line:
        # Extrae el nombre del dispositivo
        device_name = line.split(":")[2].strip()
        # Extrae el ID del dispositivo
        device_id = line.split(":")[0].strip()
        # Almacena la información en el diccionario
        devices[device_name] = device_id
#si es nvidia, poner sudo pacman -S nvidia nvidia-utils nvidia-settings
#si es amd, poner sudo pacman -S amd-ucode

# Imprime la lista de dispositivos gráficos
print("Dispositivos gráficos:")
for device, device_id in devices.items():
    print(f"{device}: {device_id}")

# Puedes utilizar el ID del dispositivo para buscar drivers
# Por ejemplo, utilizando el comando "pacman -Ss" para buscar paquetes
for device, device_id in devices.items():
    print(f"Buscando drivers para {device}...")
    driver_search = subprocess.check_output(["pacman", "-Ss", device_id]).decode()
    print(driver_search)

if "Nvidia" in lspci:
    print("pone : sudo pacman -S nvidia nvidia-utils nvidia-settings") 
elif "AMD" in lspci: print("pone: sudo pacman -S amd-ucode ")
else:
     print:("no hay nada detectable x ahora")

# quiero que muestre los resultados de lspci y los de como una
# lista de drivers o que la busque
