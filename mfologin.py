i=1
login = "mikiudalomisie"
haslo = "mikiudalomisiea"
plik = open('Loginy.txt', 'w')
for i in range (1,11):
    login = login + str(i)
    haslo = login + str(i)
    loginy = []
    loginy.append(login)
    hasla = []
    hasla.append(haslo)
    plik.write("\n1: ")
    plik.writelines(loginy)
    plik.write("\n2: ")
    plik.writelines(hasla)

plik.close()
    
    