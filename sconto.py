spesa = []
animale = []
totSpesa = 0
totAnimali = 0
totSpesaSenzaAnimali = 0  

articolo = int(input("Inserisci il prezzo di un articolo (inserisci -1 per terminare): "))
tipologia = input("Inserisci la tipologia dell'articolo, 'Y' per animale 'N' per altro: ")

while articolo != -1:
    spesa.append(articolo)
    totSpesa += articolo  

    animale.append(tipologia)
    if tipologia == 'Y':
        totAnimali += 1
    else:
        totSpesaSenzaAnimali += articolo  

    articolo = int(input("Inserisci il prezzo di un altro articolo (inserisci -1 per terminare): "))
    if articolo == -1:
        break
    tipologia = input("Inserisci la tipologia dell'articolo, 'Y' per animale 'N' per altro: ")


print("Lista degli articoli acquistati:", spesa)
print("Totale spesa:", totSpesa)
print("Totale articoli per animali:", totAnimali)
print("Totale spesa senza gli animali:", totSpesaSenzaAnimali)
print("sconto dei prodotti esclusi animali: ", totSpesaSenzaAnimali * 0.2)
print("totale spesa con sconto applicato: ", totSpesa - (totSpesaSenzaAnimali * 0.2))


