from socket import timeout
import time
from colorama import init
from termcolor import colored
import scapy.all as scapy

# Se reciben puerto e ip una vez recibidos empieza el escaner con una serie de flags definidas
# el paquete que se monta sale de un puerto aleatorio de la máquina origen y llega al puerto especificado en
# la destino se define un timeout para que no quede en bucle infinito, realizado esto se comprueba el resultado del escaner
# de tal manera que si los puertos estan abiertos es porque en la capa TCP respondieron con el flag 0x12 SYN + ACK


def scanTCP(ip, puertos):

    flags = ['S', 'SA', 'FPU', '']
    abierto = False
    for flag in flags:
        resultado = None
        resultado = scapy.sr1(scapy.IP(
            dst=ip)/scapy.TCP(sport=scapy.RandShort(), dport=int(puertos), flags=flag), verbose=0, timeout=3)

        if str(type(resultado) == "<class 'NoneType'>"):
            pass
        elif (resultado.haslayer(scapy.TCP) and resultado.getlayer(scapy.TCP).flags == 0x12):
            print("puerto/tipo\t\tstatus\n" + puertos + "/tcp\t abierto")
        elif (resultado.haslayer(scapy.ICMP) and resultado.getlayer(scapy.ICMP).flags == 0x14):
            pass


def scanUDP(ip, puertos):
    resultado = None
    resultado = scapy.sr1(scapy.IP(
        dst=ip)/scapy.UDP(sport=scapy.RandShort(), dport=int(puertos)), verbose=0, timeout=3)
    time.sleep(1)
    if resultado == None:
        print("puerto/tipo\t\tstatus\n" + puertos + "/udp\t abierto")
    elif str(type(resultado) == "<class 'NoneType'>"):
        pass
    elif resultado.haslayer(scapy.UDP):
        print("puerto/tipo\t\tstatus\n" + puertos + "/udp\t abierto")
    elif resultado.haslayer(scapy.ICMP):
        if int(resultado.getlayer(scapy.ICMP).type) == 3 and int(resultado.getlayer(scapy.ICMP).code == 3):
            pass
        elif int(resultado.getlayer(scapy.ICMP).type) == 3 and int(resultado.getlayer(scapy.ICMP).code in [1, 2, 9, 10, 13]):
            pass


def scan(ip, puerto, bool_tcp, bool_udp):

    if bool_tcp:
        scanTCP(ip, puerto)
    if bool_udp:
        scanUDP(ip, puerto)
