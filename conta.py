saluto = "ci vediamo puntuali domani mattina"
lista = list(saluto)
insieme = set(lista)
occorrenza = {} #chiave sara lettera, il valore il conteggio?
#creiamo un dizionario con le lettere di saluto

occorrenza = {}       #chiave sara lettera, il valore il conteggio
for lettera in insieme:
    occorrenza[lettera] = 1   #conta le occorrenze
    pos = saluto.find(lettera)
    if lettera in saluto[pos+1:]:
    pos = saluto[pos+1:].find(lettera)
    
    occorrenza[lettera] += 1  #incrementa il conteggio
    print(lettera, pos)    #stampa la lettera e la posizione



    def conta(stringa):
  return(["i", "a"], {"b", "c"}, {a: 5, d:2, e:1})
