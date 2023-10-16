lista = [10,6,4,9,3,2,1,5,7,8]
print("Aqui está a sua Lista:" ,    lista)
lista.sort()
print("Lista em ordem crescente:" , lista)

soma = sum(lista)
print( "A soma da lista é :" , soma)

maximo = max(lista)
print("O maior numero da lista é :" ,maximo)

minimo = min(lista)
print("O menor numero da lista é :" ,minimo) 

for i in lista:
    if i % 2 == 0:
        print("Este numero é par :" ,i)
