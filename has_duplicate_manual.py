
def has_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == "__main__":
   
    test_cases = [
        ([1, 2, 3, 4], False),
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4, 5, 6, 1], True),
        ([], False),
        ([1], False),
        ([1, 1], True),
        ([99, 99], True),
        ([1, 2, 3, 4, 5], False),
    ]
    
    print("Testando has_duplicate (MANUAL):\n")
    for nums, esperado in test_cases:
        resultado = has_duplicate(nums)
        status = "✓ PASSOU" if resultado == esperado else "✗ FALHOU"
        print(f"{status} | Input: {nums} | Esperado: {esperado} | Obtido: {resultado}")
