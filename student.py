#realizzare una classe student che rappresenti uno studente. in questo esercizio uno studente ha un nome e un punteggio totale(score) nei questionari(quiz) definite nella classe un costruttore appropriato
#e i metodi GetName() .addQuiz(score, getTOtalscore(), getAverageScore(). Per realizzare l'ultimo dei metodi richiesti, che calcola il punteggio medio x i questionari compilati dallo studente e necessario memoriazzare anche il numero di questionari


class student :
  def __init__ (self, nome , cognome) : #costruttore
    self.__nome = nome
    self.__cognome = cognome
    self.__totale_score = 0  #contatore
    self.__totale_quiz = 0   #contatore
def getName(self) : #NOME E COGNOME
  return f"{self.__nome} {self.__cognome}"
def addQuiz(self, score) :
  self.__totale_score += score  #incrementa
  self.__totale_quiz += 1  #incrementa 
def getTotalScore(self) : 
  return self.__totale_score
def getAverageScore(self) :
  return  self.__totale_score / self.__totale_quiz 

lesly = student("lesly", "vera")
sofia = student ("sofia", "ganoa")

sofia.addQuiz(100) #IL VOTO CHE HA PRESO 
print(sofia.getName())    #STAMPIAMO IL NOME E COGNOME         
print(sofia.getTotalScore())     #TOTALE   
print(sofia.getAverageScore())     #TOTALE
  
    
    
