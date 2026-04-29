def has_duplicate(numbers: list) -> bool:
    """
    Verifica se uma lista contém elementos duplicados.

    Args:
        numbers: Lista de elementos a ser verificada.

    Returns:
        True se houver duplicatas, False caso contrário.
    """
    return len(numbers) != len(set(numbers))


# Uso da função
if __name__ == "__main__":
    sample_numbers = [1, 2, 3, 4, 3]

    has_duplicates = has_duplicate(sample_numbers)

    print(f"A lista {sample_numbers} tem duplicatas? {has_duplicates}")