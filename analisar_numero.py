def analisar_numeros(lista):
    if not lista:
        return "Lista vazia"

    soma = sum(lista)
    media = soma / len(lista)
    maior = max(lista)
    menor = min(lista)

    return {
        "soma": soma,
        "media": media,
        "maior": maior,
        "menor": menor
    }



numeros = [10, 5, 8, 20, 3]
resultado = analisar_numeros(numeros)

print(resultado)