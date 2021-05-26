import crawler
import argparse
import scannerARP
import bruteforceDir
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
    parser.add_argument("-t ", "--target ", dest="ip",
                        help="Especifica una ip o rango de ips")
    parser.add_argument("-url ", dest="url",
                        help="Especifica una url")

    return parser.parse_args()


argumentos = get_argumentos()
print(argumentos)

if argumentos.scanerarp:
    if not argumentos.target:
        print("Se necesitan más argumentos para el scaner prueba con python3 hellHound -h")
        exit()
    else:
        resultados = scannerARP.scan(argumentos.target)
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
