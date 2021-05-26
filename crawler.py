
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
from urllib import error

#Spider que se saca cada uno de los links de la página actual mediante 
#el módulo BeautifulSoup en el que encuentra los elementos de tipo a div y los scripts
def crawl(bsObj):
    lista_links = []
      
    for link in bsObj.find_all('a'):
        if 'href' in link.attrs:
            if link.attrs['href'] and link.attrs['href'][0] != '#':
                lista_links.append(link.attrs['href'])
    for link in bsObj.find_all('script'):
        if 'src' in link.attrs:
            print("script " + link.attrs['src'])

        return list(set(lista_links))

def spider(url):

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    aux = urlopen(req, timeout = 10)
    bsObj = soup(aux.read(), features="lxml")
    links_sin_visitar = crawl(bsObj)

    for link in links_sin_visitar:
        print("href: " + link)

    for link in links_sin_visitar:
        if link.find("http") != -1:
            try:
                req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
                aux = urlopen(req, timeout = 10)
                print (aux.getcode())
                bsObj = soup(aux.read(), features="lxml")
                links_visitados = crawl(bsObj)
                if links_visitados:
                    for link2 in links_visitados:
                        print("href: " + link2)
            except (error.URLError, error.HTTPError):
                print ("Timeout")
                continue
            
