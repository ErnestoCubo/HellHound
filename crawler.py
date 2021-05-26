from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

#Spider que se saca cada uno de los links de la página actual mediante 
#el módulo BeautifulSoup en el que encuentra los elementos de tipo a div y los scripts
def spider(url):

    pagina = 1
    aux = urlopen(url)
    bsObj = soup(aux.read(), features="lxml")

    for link in bsObj.find_all('a'):
        if 'href' in link.attrs:
            if link.attrs['href'][0] != '#':
                print("href " + link.attrs['href'])
    for link in bsObj.find_all('div'):
        if 'href' in link.attrs:
            if link.attrs['href'][0] != '#':
                print("href " + link.attrs['href'])
    for link in bsObj.find_all('script'):
        if 'src' in link.attrs:
            print("script " + link.attrs['src'])
