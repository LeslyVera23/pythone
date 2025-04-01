aliquota1 = 0.23
aliquota2 = 0.35
aliquota3 = 0.43
scaglione_1 = 28000
scaglione_2 = 50000
scaglione_3 = scaglione_1 * aliquota1
imposta_lorda = 0 #qui utente ti dira imposta lorda
reddito = int(input("inserisci il reddito: "))
if reddito <= 28000:
    imposta_lorda = reddito * aliquota1
else:
    if reddito > 28000 and reddito <= 50000:
        imposta_lorda = (scaglione_1 * aliquota1 + (reddito - scaglione_1) * aliquota2)
    else:
        imposta_lorda = (scaglione_1 * aliquota1 + (scaglione_2 - scaglione_1) * aliquota2 + (reddito - scaglione_2) * aliquota3)
    print("l'imposta totale da pagare è: ", imposta_lorda)




