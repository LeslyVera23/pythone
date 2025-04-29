from bs4 import BeautifulSoup #importiamo libreria

html_compatto = "<html>" \
"<body>" \
"<h1>Titolo prova python</h1>" \
"<p>questo è un paragrafo</p>" \
"</body>" \
"</html>"

html_compatto = "".join(x.strip() for x in html.split("\n"))   #rimuove gli spazi vuoti e le righe vuote
print(html_compatto)       #mostra il codice HTML compatto in una sola riga

doc = BeautifulSoup(html_compatto, "html.parser")
print(doc.prettify())     #formatta il codice html

root = doc.html
print(type(root))          #elemento tag
print(root.name.upper())   #struttura html
print(root.name.lower())   #struttura html