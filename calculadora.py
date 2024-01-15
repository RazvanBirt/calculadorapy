#funçao média
def average_list(lista):
    media = sum(lista) / len(lista)
    return media

#criar lista de 10 numeros
numeros = [2, 5, 7, 5, 9, 12, 20, 18, 19,]

media = average_list(numeros)
print(f"A media é {media}")