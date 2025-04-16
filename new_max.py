#scrivere un programma python che acquisista tutte le righe di un file di testo (.txt) il cui nome va richiesto all'utente. il file si suppone contenere un numero per ogni righa(anche con decimali) float
#calcolare la media e indicare il valore massimo comprenssivo della riga in cui e stato trovato nel file
#quindi chiedere massimo 3 numeri cosi da dopo fare la media

#chiediamo all'utente nome del file
def main () :
   #chiedi utente nome file
  nome_file = input("inserisci il nome del tuo file: ") 
  #apertura file
  infile = open( nome_file , "r") 
  linee = infile.readLines()  #da invocare
  infile.close()
  for linea in linee :
    print(linea)




