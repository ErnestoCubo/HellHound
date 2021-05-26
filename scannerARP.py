#!/usr/bin/env python

import scapy.all as scapy

# Primero se crea el paquete arp a la ip luego se crea un paquete de tipo broadcast
# que circula por la red y más tarde se envían y reciben paquetes creando así dos listas
# una vez creadas ambas listas en caso de que no se reciban paquetes se pone un timeout de 1
# las listas contienen host respondidos y host no respondidos, luego con los que contestaron
# se crea un diccionario con los únicos datos que interesan de los que se reciben en este caso
# solo me interesam sus ips y sus macs


def scan(ip):

    paquete_arp = scapy.ARP(pdst=ip)
    paquete_Broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    paquete_mixto = paquete_Broadcast/paquete_arp
    host_activos, host_inactivos = scapy.srp(paquete_mixto, timeout=1)

    host_list = []

    for host in host_activos:
        host_dict = {
            "ip": host[1].psrc,
            "mac": host[1].hwsrc
        }
        host_list.append(host_dict)
    return host_list


def print_resultado(host_list):
    print("Mostrando Hosts Activos")
    print("IP\t\t\tMAC\t")
    for host in host_list:
        print(host["ip"] + "\t\t" + host["mac"])
