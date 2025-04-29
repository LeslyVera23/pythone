
from bs4 import BeautifulSoup #importiamo libreria
doc = bs4.BeautifulSoup(html_compatto)  #analizza il contenuto HTML della pagina
def naviga3(tag):
    if tag.name.upper() == "A":
        print(tag.get("href"))
    for stag in tag.contents:
        if type(stag) == bs4.element.Tag :
            naviga3(stag)
            naviga3(doc)
            naviga3(tag)