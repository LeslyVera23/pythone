somma = 0
numeri_letti = 0
valore_stringa = input("Passami il prossimo valore oppure 'exit': ")
while valore_stringa != "exit":
    numeri_letti += 1
    somma += int(valore_stringa)
    valore_stringa = input("Passami il prossimo valore oppure 'exit': ")
#print("Numeri letti sono : ", numeri_letti)
#print("La somma dei numeri è : ", somma)
print("La media dei numeri letti è: ", somma / numeri_letti)



