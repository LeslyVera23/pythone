#acquisire l'inpuit da utente controllando se il contennuto della stringa puo essere interpretato come una data. restituirlo con ('print') con un formayo standard'
#esempio 3/3/25 => 03-03-2025
#7-5-24 => 05-05-2024
#29/03 => 29-03-25
nomeRegione = "marche"
for letter in nomeRegione :
    print(letter)


for pos in range(1, 10) :
 print(pos)

#for y in range(1,4):
   #for x in range(1, 4):
     # print(x*y)
      #print("--")

regione = "Trentino Alto Adige"
indice = 0
indice = regione.find(" ", indice)
print(indice)
indice += 1
indice = regione.find(" ", indice)
print(indice)
indice += 1
indice = regione.find(" ", indice)
print(indice)


