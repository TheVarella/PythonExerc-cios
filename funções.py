#def nome_da_função (parâmetros):
#<instruções>
#return "valor do retorno"

#a palavra "def" determina o início da função
#parâmetros são informações que a função pode receber para o seu processamento.
#os parâmetros podem existir ou não
#o corpo da função é o local em que é aplicada a sequência de instruções, como entrada, processamento e/ou saída
#return deve ser utilizado quando houver necessidade de retornar alguma informação para a ação da função

def lernotas():
    n = float(input("Digite uma nota para o aluno: "))
    return n

def resultado(n1,n2):
        media = (n1+n2)/2
        print("Nota 1: ", n1)
        print("Nota 2: ", n2)
        print("Média: ", media)
        print("Resultado: ", end="")
        if media >= 7:
            print("Aprovado!")
        else:
            print("Reprovado!")

            a = lernotas()
            b = lernotas()
            resultado(a,b)



