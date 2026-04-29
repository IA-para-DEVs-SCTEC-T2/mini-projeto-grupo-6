def tem_duplicados(lista):
    return len(lista) != len(set(lista))


# Teste
numeros = [10, 5, 8, 20, 3, 5]
print(tem_duplicados(numeros))  # True