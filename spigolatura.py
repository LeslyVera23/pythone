import urllib.request
import bs4
url = "https://amabilejewels.it/?srsltid=AfmBOopHJIjoHBn7kZ_hnPgr1HCApo-jHAisa_YU46n25RLjnB2e34lx"
risultato = urllib.request.urlopen(url)  #Esegui la richiesta e apri la pagina
theBytes = risultato.read()              #Legge il contenuto della pagina
text = theBytes.decode()                 #Decodifica il contenuto in bytes della stringa 
doc = bs4.BeautifulSoup(text, 'html.parser')  #analizza il contenuto HTML della pagina
print(doc.prettify())                    #stampa il contenuto in html
