
class stanza:
  self_ampiezza = DIM1
  self_profondita = dim2
  def ampiezza(self) :
    return self_ampiezza
    def profondita (self)
    return self_profondita
    def area(self)
    return self_ ampiezza * self_profondita
   # def __repr__(self):
      #return "in fase di sviluppo"
  def __repr__(self):
      return f"stanza di dimensioni (self._ampiezza) x {self._profondita}"
    



cucina = stanza(4,5)
bagno = stanza(3,2)
salone = stanza(4,6)
print(cucina.profondita())

print(cucina)
#se volessi personalizzare la print, vuoldire andare ricoprire i metodi.
#__set -> undercorde serve per dire sono temporanei
nuova_istanza_generica = object()       #object crea un oggeto base , derivano tutti gli altri oggetti 
print(nuova_istanza_generica)
