from socket import timeout
import time
from colorama import init
from termcolor import colored
import scapy.all as scapy
import re

# El escaner funciona de dos manera de manera en la que se pase la flag en la que el se 
# quiera ver los puertos filtrados por el firewall o un modo agresivo en el que se
# realizar el scaner dejando algo de rastro pero solo se puede saber si esta cerrado o 
# abierto el puerto,
def scanTCP(ip, puertos, tipo):

    dst_ip = ip
    puerto_origen = scapy.RandShort()
    puerto_destino = int(puertos)
    paquete_TCP = scapy.TCP(sport=puerto_origen,
                            dport=puerto_destino, flags="S")
    paquete_IP = scapy.IP(dst=dst_ip)

    if tipo == "a":

        scan_resp = scapy.sr1(paquete_IP/paquete_TCP, verbose=0, timeout=10)
        if(str(type(scan_resp)) == "<type 'NoneType'>"):

            print(str(puerto_destino) + "\ttcp\t\t cerrado")
        elif scan_resp.haslayer(scapy.TCP) and scan_resp.getlayer(scapy.TCP).flags == 0x12:

            paquete_TCP = scapy.TCP(
                sport=puerto_origen, dport=puerto_destino, flags="AR")
            send_rst = scapy.sr(paquete_IP/paquete_TCP, verbose=0, timeout=10)
            print(str(puerto_destino) + "\ttcp\t\t abierto")
        elif (scan_resp.getlayer(scapy.TCP).flags == 0x14):

            print(str(puerto_destino) + "\ttcp\t\t cerrado")

    elif tipo == "fw":

        scan_resp = scapy.sr1(paquete_IP/paquete_TCP, verbose=0, timeout=10)
        if(str(type(scan_resp)) == "<type 'NoneType'>"):

            print(str(puerto_destino) + "\ttcp\t\t filtrado por fw")
        elif scan_resp.haslayer(scapy.TCP) and scan_resp.getlayer(scapy.TCP).flags == 0x12:

            paquete_TCP = scapy.TCP(
                sport=puerto_origen, dport=puerto_destino, flags="R")
            send_rst = scapy.sr(paquete_IP/paquete_TCP, verbose=0, timeout=10)
            print(str(puerto_destino) + "\ttcp\t\t abierto")
        elif (scan_resp.getlayer(scapy.TCP).flags == 0x14):

            print(str(puerto_destino) + "\ttcp\t\t cerrado")
        elif(scan_resp.haslayer(scapy.ICMP)):

            if(int(scan_resp.getlayer(scapy.ICMP).type) == 3 and int(scan_resp.getlayer(scapy.ICMP).code) in [1, 2, 3, 9, 10, 13]):

                print(str(puerto_destino) + "\ttcp\t\t filtrado por fw")


def scan(ip, puerto, bool_tcp, tipo_scan_tcp):

    print("puerto\ttipo\t\tstatus\n")

    if puerto.find(",") != -1:

        str(puerto)
        puerto_inicio, puerto_final = re.split(',', puerto)
        puertos_escanear = int(puerto_final) - int(puerto_inicio)

        i = 0
        while i <= puertos_escanear:

            if i == 0:

                scanTCP(ip, puerto_inicio, tipo_scan_tcp)
            else:

                scanTCP(ip, str(int(puerto_inicio) + i), tipo_scan_tcp)
            i += 1

    elif puerto.find(":") != -1:

        str(puerto)
        puertos = []
        puertos = re.split(':', puerto)

        for port in puertos:

            scanTCP(ip, port, tipo_scan_tcp)
    else:

        scanTCP(ip, puerto, tipo_scan_tcp)
