def has_duplicate(nums):
    lista = []

    for num in nums:
        if num in lista:
            return True
        lista.append(num)
    return False

# uso da função
numeros = [1, 2, 3, 4, 2]

resultado = has_duplicate(numeros)

print(resultado)