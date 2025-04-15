#realizzare una classe sodacam che rappresenti una lattina di bibta(quindi di forma cilindrica), dotata di metodi
#getSurfaceArea() e getVolume #pass metti cosi non ti da errore mentre fa la compilazione
#il costruttore riceve come argomento l'altezza e il raggio della base della lattina.
import math   #prendi nella libreria python
class  sodaCan : #crei la classe del oggetto
  def  __init__(self, altezza, raggio ) :   #costruttore con i parametri, si attiva quando si crea oggetto
    self.__altezza = altezza #salva l’altezza nell’oggetto
    self.__raggio = raggio  #salva raggio nell’oggetto
  def getSurFaceArea(self) :  #calcola l’area della superficie della lattina
    circonferenza = 2 * math.pi * self._raggio
    laterale = self._altezza * circonferenza
    area_base = math.pi * self._raggio ** 2
   return laterale + 2 * area_base
  def getVolume(self) :   #calcola il volume del cilindro
    area_base = math.pi * self._raggio ** 2
    return self._altezza * area_base

mini_lattina = sodaCan(7.6, 2.5)  #primo oggetto
lattina = sodaCan(9.24 , 3.37)   #secondo oggetto

print(mini_lattina.getSurFaceArea())  #area
print(lattina.getSurFaceArea())       #area
print(mini_lattina.getVolume())       #volume
print(lattina.getVolume())            #volume





    
  
