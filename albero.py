#ricevuti in input: un carattere da utilizzare, ampiezza di base. Rappresentare l' albero.
stringa = input("Passami un carattere: ")
base = int(input("Passami ampiezza della base: "))

#print(stringa * base)
#print("" * 2 + "A" * 1)
#print("" * 2 + "A" * 3)
#print("" * 2 + "A" * 5)

char = input("carattere da ripetere: ")
base = int(input("ampiezza della base: "))
i = 1
while i <= base :
    print("" * ((base - i) // 2 ) +
        char * (i + 1 - (base % 2)))
    i += 2