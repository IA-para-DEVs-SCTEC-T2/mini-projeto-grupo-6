
def has_duplicate(nums):
   
    if not nums or len(nums) <= 1:
        return False

    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)

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
    
    print("Testando has_duplicate (GERADA PELA IA):\n")
    for nums, esperado in test_cases:
        resultado = has_duplicate(nums)
        status = "✓ PASSOU" if resultado == esperado else "✗ FALHOU"
        print(f"{status} | Input: {nums} | Esperado: {esperado} | Obtido: {resultado}")