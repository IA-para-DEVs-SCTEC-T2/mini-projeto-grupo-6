def has_duplicate(nums);
    lista = []
    
    for num in nums:
        if num is lista:
            return True
        lista.append(num)
    return false

# uso da função
numeros = [1,2,3,4]

resultado = has_duplicate(numeros)

print(resultado)