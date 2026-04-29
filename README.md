# mini-projeto-grupo-6

## Comparativo de legibilidade: `has_duplicate`

Duas implementações da mesma função foram desenvolvidas para fins de comparação.

### duplicata_manual.py — Implementação manual

```python
def has_duplicate(nums):
    lista = []
    for num in nums:
        if num in lista:
            return True
        lista.append(num)
    return False
```

Mais verbosa, porém didática. O passo a passo é explícito: cria uma lista auxiliar, itera sobre os elementos e verifica manualmente se cada um já foi visto. Boa para quem está aprendendo lógica de programação, pois deixa claro o que acontece em cada etapa.

### duplicata_ia.py — Implementação com recurso nativo

```python
def has_duplicate(nums):
    return len(nums) != len(set(nums))
```

Mais concisa e idiomática. Usa `set()`, estrutura nativa do Python que elimina duplicatas automaticamente. A comparação de tamanhos resolve o problema em uma única linha. Mais legível para desenvolvedores experientes em Python, e tende a ter melhor desempenho em listas grandes.

### Conclusão

| Critério         | Manual                  | Com set()              |
|------------------|-------------------------|------------------------|
| Linhas de código | 6                       | 1                      |
| Legibilidade     | Alta para iniciantes    | Alta para experientes  |
| Desempenho       | O(n²) no pior caso      | O(n)                   |
| Pythônico        | Não                     | Sim                    |
