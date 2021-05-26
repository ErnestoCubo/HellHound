import crawler
import argparse
import scannerARP
import bruteforceDir
import portScanner
cabezal = """

         ((((,                /#
         ((.(((.((. .     ,(###                       .
          (( ((((( .((((##########               %%#%&
  (.*((((,((**(((((( ((((##################%%%%%%%%%           ..
    /((( /,(* (((((((  (####################%%%%%&
      ( (((((  (/     ,#(,  ######   %#######%%%%%%%%%%%%&.
        (((((((((((((((((#   #(######     ##%%%%%%%%%%
       (((((,((((( ((((((##### #########    %%%%%%%%%%%%.
       ,(((( ( ( ((((((((####### ###### %%    %%%%% &%%%%%&
        ((((  ((((.#((((((###/    #######       %%%%   %%%%%%
       .((*//( (  (((((#*####### ########## &%  #%%%%( %%%%%%%%&
        (((    ( ((((((. #(##     #########& *%% %%%%%%  %%%%%%%%%%%&
          (((*((((((((((######  ( #########   %%%%%%/%%%  %%
          (((((((((((((((  (##  #(######* #% %%%%%%% %%%  %%&
         ((((((((((((((((,(##( %########    #%%%%%%       %%%
        ((((((((((( #(((((( ###########, ####%%%%%%       %%%
        ((((((((/(/(    (  ##(######## %##### %%%%%  %%%  ,%%
       (((((((((/((    (.#((#### #%  %######% #%%%&  %%%%%%%%* ..
         (,((/(((   ((((( ( ###* /(###### ###  #%   ,%%%%%%%%%
                  ((((((#, ##.########%  /# %      (%%/   &%%%.
                   ((((((( # ########  # , ###    %%%
                    *((((( ,##.##### /(#  #% ## .%%%
                 .  (((((((((#  (#  # #%%#  %##%%&  .
                    ((  (((  #   ### ###   %##%
                             ( ##(  ##    %
                            ###
                          ##

               _  _                                   _
        /\  /\  ___ | || |  /\  /\  ___   _   _  _ __    __| |
      / /_/ / / _ \| || | / /_/ / / _ \ | | | || '_ \  / _` |
      / __  / |  __/| || |/ __  / | (_) || |_| || | | || (_| |
      \/ /_/   \___||_||_|\/ /_/   \___/  \__,_||_| |_| \__,_|


"""

print(cabezal)


def get_argumentos():
    # Parser argumentos
    parser = argparse.ArgumentParser(description="HellHound")

    parser.add_argument("-arp", "--scanerarp", action="store_true", default=False,
                        help="Realiza un escaneo de red para encontrar ips activas en la red")
    parser.add_argument("-crw", "--crawler", action="store_true", default=False,
                        help="Realiza spidering sobre la url indicada")
    parser.add_argument("-dsh", "--hellsearch", action="store_true", default=False,
                        help="Realiza un fuzzing a la url indicada necesita el parametro -wrdl")
    parser.add_argument("-wrdl ", "--wordlist ", dest="worldistPath",
                        help="Especifica un diccionario")
    parser.add_argument("-pscan", "--portScaner", action="store_true",
                        default=False, help="Realiza un scaner de puertos")
    parser.add_argument("-tg ", "--target ", dest="ip",
                        help="Especifica una ip o rango de ips")
    parser.add_argument("-url ", dest="url",
                        help="Especifica una url")
    parser.add_argument("-tcp", action="store_true", default=False,
                        help="Realiza el escaner de puertos en los puertos TCP")
    parser.add_argument("-p", "--port", dest="puerto",
                        help="Especifica un puerto o rango de puertos en caso de rango de puertos [<puerto_inicio>,<puerto_final>], para puertos espcificos [<puerto_a>:<puerto_b>:<puerto_c>]")
    parser.add_argument("-a", action="store_true", default=False,
                        help="Realiza el escaner de puertos TCP de manera agresiva")
    parser.add_argument("-fw", action="store_true", default=False,
                        help="Realiza el escaner de puertos TCP filtrados por el fw")

    return parser.parse_args()


argumentos = get_argumentos()

if argumentos.scanerarp:

    if not argumentos.ip:

        print("Se necesitan más argumentos para el scaner prueba con python3 hellHound -h")
        exit()
    else:

        resultados = scannerARP.scan(argumentos.ip)
        scannerARP.print_resultado(resultados)
elif argumentos.crawler:

    if not argumentos.url:

        print(
            "Se necesitan más argumentos para el crawler prueba con python3 hellHound -h")
        exit()
    else:

        crawler.spider(argumentos.url)
elif argumentos.hellsearch:

    if not argumentos.url:

        print(
            "Se necesitan más argumentos para el crawler prueba con python3 hellHound -h")
        exit()
    elif not argumentos.worldistPath:

        print(
            "Se necesitan más argumentos para el crawler prueba con python3 hellHound -h")
        exit()
    else:

        bruteforceDir.main(argumentos.url, argumentos.worldistPath)
elif argumentos.portScaner:

    if not argumentos.puerto:

        print(
            "Se necesitan más argumentos para el crawler prueba con python3 hellHound -h")
        exit()
    else:

        if not argumentos.ip:

            print(
                "Se necesitan más argumentos para el crawler prueba con python3 hellHound -h")
            exit()
        else:
            if argumentos.fw:

              portScanner.scan(argumentos.ip, argumentos.puerto,
                              argumentos.tcp, "fw")

            elif argumentos.a:

                            portScanner.scan(argumentos.ip, argumentos.puerto,
                              argumentos.tcp, "a")
            
            else:

              portScanner.scan(argumentos.ip, argumentos.puerto,
                              argumentos.tcp, '')
