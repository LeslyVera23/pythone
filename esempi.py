#print(greca[len(greca) -1])
#print(greca[-1])

#nome = "andrea ribuoli"
#print(nome.upper() + "/n" + nome.lower())
formato = "%3d %-26s 10%% %9.2f"
print("Qta Prodotti IVA TOTALE\n" +
formato % (2, "Hamburger", 2.8) + "\n" +
formato % (1, "6 McNuggets", 4.9) + "\n" +
formato % (1, "McMenu Large Big Mac", 8.8))