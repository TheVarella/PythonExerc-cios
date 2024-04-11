arquivo = open("arqTxt.txt", "w")

arquivo.write("Curso Python \n")
arquivo.write("Aula Prática")
arquivo.close()

leitura = open("arqTxt.txt", "r")
print(leitura.read())
leitura.close()

