def has_duplicate(nums):
    """
    Verifica se há elementos duplicados em uma lista.

    Abordagem manual: percorre a lista elemento por elemento,
    mantendo um registro dos números já visitados.
    Se o número atual já estiver na lista auxiliar, há duplicata.

    Parâmetros:
        nums (list): lista de números a ser verificada

    Retorna:
        bool: True se houver duplicata, False caso contrário
    """
    lista = []  # lista auxiliar para armazenar os números já visitados

    for num in nums:
        if num in lista:  # verifica se o número já foi encontrado antes
            return True
        lista.append(num)  # adiciona o número à lista de visitados

    return False  # nenhum duplicado encontrado

# uso da função
numeros = [1, 2, 3, 4, 2]

resultado = has_duplicate(numeros)

print(resultado)
