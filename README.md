# mini-projeto-grupo-6

## Análise Comparativa: `has_duplicate` vs `has_duplicate_refactor`

### Implementações

**Original:**
```python
def has_duplicate(lst):
    return len(array) != len(set(array))
```

**Refatorada:**
```python
def has_duplicate_refactor(lst):
    seen = set()
    return any(x in seen or seen.add(x) for x in lst)
```

---

### Correção de Bug

A versão original contém um bug: referencia a variável `array` em vez do parâmetro `lst`, causando `NameError` em tempo de execução. A versão refatorada corrige esse problema.

---

### Complexidade de Tempo

| Caso         | Original `O(n)` | Refatorada `O(k)` |
|--------------|:--------------:|:-----------------:|
| Melhor caso  | O(n)           | O(1) a O(k)       |
| Pior caso    | O(n)           | O(n)              |

- **Original:** converte a lista inteira em `set` antes de qualquer comparação — sempre percorre todos os `n` elementos, mesmo que a duplicata esteja na segunda posição.
- **Refatorada:** usa `any()` com avaliação *short-circuit*, interrompendo a iteração assim que a primeira duplicata é encontrada. Em listas com duplicatas no início, isso representa ganho significativo.

---

### Complexidade de Espaço

Ambas alocam um `set` auxiliar de tamanho proporcional à quantidade de elementos únicos — complexidade de espaço **O(n)** no pior caso.

A versão refatorada constrói o `set` incrementalmente, podendo usar menos memória quando há duplicatas no início da lista.

---

### Legibilidade

| Critério          | Original | Refatorada |
|-------------------|:--------:|:----------:|
| Linhas de código  | 1        | 2          |
| Clareza de intenção | Alta   | Média      |
| Idioma Pythônico  | Sim      | Sim        |

A versão original é mais direta e fácil de entender à primeira vista. A versão refatorada exige conhecimento do efeito colateral de `set.add()` retornar `None` para compreender o truque do `any()`.

---

### Quando usar cada uma

- **Original** (corrigida): prefira quando a lista for pequena ou quando a clareza do código for mais importante que a performance.
- **Refatorada**: prefira quando a lista puder ser muito grande e duplicatas forem prováveis no início (ex.: validações de entrada, streams de dados).
