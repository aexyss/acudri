#!/usr/bin/env python3

import subprocess

print("anal izando durowario nunca supe como se escribia")
##
lspci =subprocess.check_output(["lspci"]).decode()
print(lspci)

if "Nvidia" in lspci:
    print("pone : sudo pacman -Sy nvidia nvidia-utils nvidia-settings") 
elif "AMD" in lspci:("pone: sudo pacman -Sy amd-ucode ")
else:
     print=("no hay nada detectable x ahora")

# quiero que muestre los resultados de lspci y los de como una lista de drivers o que la busque



