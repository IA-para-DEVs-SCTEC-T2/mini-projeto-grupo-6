def has_duplicate(nums):
    return len(nums) != len(set(nums))

# uso da função
numeros = [1, 2, 3, 4, 2]

resultado = has_duplicate(numeros)

print(resultado)
