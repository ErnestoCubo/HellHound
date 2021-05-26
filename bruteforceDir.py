import socket
import requests

#Para comprobar los directorios primero creo un socket de conexión hacia la url
#Creado el socket paso a parsear el diccionarioo para más tarde poder comprobar
# con cada palabra del diccionario una url distinta y así realizar el fuzzing
def main(url, wordlist):

    print('[*]Comprobando HOST activo...')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:

        status = s.connect_ex((url, 80))
        s.close()

        if status == 0:

            print('[CORRECTO]')
            parseo_wordlist(wordlist, url)
            print('[*]Scan terminado')
            pass
        else:

            print('[FAIL]')
            print('No se pudo encontrar el host: %s' %url)
    except socket.error:
        print('[FAIL]')
        print('[!] Error: No se econtró la url especificada: %s' %url)
        exit()

def parseo_wordlist(wordlist, url):

    try:

        with open(wordlist) as file:

            checker = file.read().strip().split('\n')
        print('[Diccionario parseado]')
        print('[*] Número de paths para comprobar: %s' %(str(len(checker))))
        print('Empezando scan...')
        for path in checker:
            path_check(path, url)
    except IOError:
        print('[FAIL]')
        print('[!] Error: Fallo al leer el diccionario')
        exit()

def path_check(path,  url):

    try:

        response = requests.get('http://' + url + '/' + path).status_code
    except Exception:

        print('[!]Error inesperado')
        exit()
    if response == 200:
        
        print('Directorio encontrado %s' %(url + '/' + path))