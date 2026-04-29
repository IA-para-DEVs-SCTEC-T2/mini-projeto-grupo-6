def has_duplicate(nums):
    """
    Verifica se há elementos duplicados em uma lista.

    Abordagem com recurso nativo do Python: converte a lista em um set,
    que por definição não permite elementos repetidos.
    Se o tamanho do set for menor que o da lista original, há duplicatas.

    Parâmetros:
        nums (list): lista de números a ser verificada

    Retorna:
        bool: True se houver duplicata, False caso contrário
    """
    # set() remove automaticamente os duplicados;
    # se os tamanhos diferirem, algum elemento se repetia na lista original
    return len(nums) != len(set(nums))

# uso da função
numeros = [1, 2, 3, 4, 2]

resultado = has_duplicate(numeros)

print(resultado)
