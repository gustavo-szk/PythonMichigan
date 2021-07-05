enum = 0
maior = -1
menor = None
while True:
    enum = input("Digite um Número ")
    if enum == "fim" :
        break
    try :
        num = int(enum)
    except :
        print('Valor Errado')
    if menor is None :
        menor = num
    elif num < menor :
        menor = num
    elif num > maior :
        maior = num
print("Maximum is", maior)
print("Minimum is", menor)