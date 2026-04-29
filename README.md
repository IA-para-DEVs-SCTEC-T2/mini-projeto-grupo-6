# mini-projeto-grupo-6

**Projeto Hands-on: Humano x Máquina**

Um mini-projeto prático para comparar implementações manuais com código gerado por IA, explorando legibilidade, eficiência e boas práticas.

---

## Objetivo

Implementar uma função `has_duplicate(nums)` que verifica se há duplicatas em uma lista de inteiros, de duas formas:
1. **Manualmente** - usando sua própria lógica e criatividade
2. **Com IA** - usando Copilot/Claude/Kiro
3. **Comparar** - analisar diferenças, eficiência e qualidade

---

## Começando

### Etapa 1: Implementação Manual (20 min)

Implemente a função `has_duplicate(nums)` **SEM ajuda de IA**:

```bash
# Abra o arquivo
code has_duplicate_manual.py
```

**Requisitos:**
- ✓ Lógica correta para detectar duplicatas
- ✓ Pode ser O(n²), usar set, sort, ou outra estratégia
- ✓ Todos os testes devem passar
- ✓ Faça commit quando terminar

**Testar sua implementação:**
```bash
python has_duplicate_manual.py
```

---

### Etapa 2: Implementação com IA (5 min)

Use o Copilot/Claude/Kiro para gerar a função:

**Prompt a usar:**
```
Crie em Python uma função que verifica se há duplicatas numa lista de inteiros. 
A função deve ser eficiente e lidar com listas vazias e listas com um único elemento.
```

1. Cole o prompt no Copilot/Claude
2. Copie a resposta gerada
3. Cole em `has_duplicate_ia.py`
4. Teste se passa em todos os casos

**Testar a implementação:**
```bash
python has_duplicate_ia.py
```

**Não esqueça:** Documente o prompt usado no arquivo!

---

### Etapa 3: Análise Comparativa (5 min)

Abra o arquivo `ANALISE_COMPARATIVA.md` e:

1. Cole ambas as implementações nos blocos designados
2. Use o **prompt para análise** com o Copilot/Claude
3. Copie a resposta completa da IA no arquivo
4. Identifique pontos fortes e fracos de cada versão

**Arquivo:**
```bash
code ANALISE_COMPARATIVA.md
```

---

### Etapa 4: Aplicar Melhorias (incluído no tempo anterior)

Com base na análise:

1. **Identifique pelo menos 1 melhoria** sugerida pela IA
2. **Aplique no seu código manual** (`has_duplicate_manual.py`)
3. **Documente** o que foi melhorado em `ANALISE_COMPARATIVA.md`
4. **Teste novamente** para garantir que tudo funciona

---

## Estrutura do Projeto

```
mini-projeto-grupo-6/
├── has_duplicate_manual.py      # Sua implementação
├── has_duplicate_ia.py          # Gerada pela IA
├── ANALISE_COMPARATIVA.md       # Análise e comparação
├── README.md                    # Este arquivo
└── .git/                        # Repositório Git
```

---

## Checklist de Entrega

- [ ] **Etapa 1**: Implementação manual funcionando + commit
- [ ] **Etapa 2**: Implementação com IA funcionando + prompt documentado
- [ ] **Etapa 3**: Análise comparativa completa em Markdown
- [ ] **Etapa 4**: Pelo menos 1 melhoria aplicada ao código manual
- [ ] **Git**: 3+ commits (manual, IA, análise/melhorias)
- [ ] **README**: Preenchido e atualizado

---

## Dicas

### Sobre Implementações
- **Set approach**: O(n) de tempo, O(n) de espaço - melhor para listas grandes
- **Sort approach**: O(n log n) de tempo, O(1) de espaço - menos memória
- **Brute force**: O(n²) de tempo, O(1) de espaço - mais simples, menos eficiente

### Sobre Edge Cases
- Lista vazia `[]`
- Lista com 1 elemento `[1]`
- Duplicatas no início, meio ou fim
- Números negativos e zero
- Valores muito grandes

### Sobre Código Idiomático Python
- Use `set()` para verificações rápidas
- Use `in` para testar pertencimento
- Nomeie variáveis com clareza
- Adicione docstrings
- Use type hints

---

## Tempo Total Estimado

| Etapa | Tempo |
|-------|-------|
| 1. Manual | 20 min |
| 2. IA | 5 min |
| 3. Análise | 5 min |
| **Total** | **30 min** |

---

## Referências

- [Python Lists e Sets](https://docs.python.org/3/tutorial/datastructures.html)
- [Complexidade de Algoritmos](https://en.wikipedia.org/wiki/Big_O_notation)
- [PEP 8 - Style Guide](https://pep8.org/)

---

## Grupo 6

Desenvolvido como exercício hands-on de comparação Humano x Máquina.

**Criado em:** 28 de abril de 2026
**Branch:** feature/duplicatas

