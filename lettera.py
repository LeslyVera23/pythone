#Realizzare un classe Letter che consenta di scrivere e impaginare una semplice lettera. il costruttore riceve i nomi del mittente(letterFrom) e del destinatario(letterTO)
#def__init_(self, letterFrom, letterTo):
#realizza il metodo:
#def addLine(self, line):
#che aggiunga un riga di testo (line) al corpo della lettera, in fondo e il metodo:
#def getText(self):
#che ristituisca l'intero testo della lettera avente forma:
# dear nomeDestinatario
#riga vuota
#Prima riga del corpo della lettera
#seconda riga del corpo
#....
#ultima riga el corpo
#riga vuota
#sincerely
#riga vuota
#nomeMittente
class letter :
  def __init__(self, letterFrom,letterTO) :
    self_letterFrom = 0
    self_letterTo = 0
    self_conta_lettera = ""  #stringa vuota
  #METODO ADDLINE
  def addLine(self, line):
    conta_lettera  = conta_lettera + line  + "\n"
  def getText(self):
     return "Dear " + self.letterTo  + ":\n\n" + conta_lettera + ":\n\n" + self.letterFrom

lettera =  letter("Dear" , "jhon")
lettera.addLine("")
lettera.addLine("")
lettera.addLine("")


print(lettera.getText())



    
