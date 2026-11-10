# Documentação do módulo `calculadora`

## Visão geral

O módulo **`calculadora.py`** fornece a classe `Calculadora`, que implementa as quatro operações aritméticas básicas:

- soma
- subtração
- multiplicação
- divisão (com tratamento de divisão por zero)

Todos os métodos são **estáticos**, pois não há necessidade de manter estado entre as chamadas. Cada método aceita dois operandos do tipo `float` (ou qualquer tipo que suporte as operações aritméticas) e devolve o resultado também como `float`.

---

## Classe `Calculadora`

```python
class Calculadora:
    """Classe que implementa operações aritméticas simples.

    Todos os métodos são estáticos porque não há necessidade de manter
    estado entre as chamadas. Cada método recebe dois operandos do tipo
    ``float`` (ou qualquer tipo que suporte as operações aritméticas) e
    devolve o resultado também como ``float``.
    """
```

### Métodos estáticos

| Método        | Assinatura                                 | Descrição                                                        | Exemplo de uso                              |
|---------------|--------------------------------------------|------------------------------------------------------------------|---------------------------------------------|
| `somar`       | `somar(a: float, b: float) -> float`       | Retorna a soma de `a` e `b`.                                     | `Calculadora.somar(2, 3)  # → 5`            |
| `subtrair`    | `subtrair(a: float, b: float) -> float`    | Retorna a diferença `a - b`.                                     | `Calculadora.subtrair(5, 2)  # → 3`         |
| `multiplicar` | `multiplicar(a: float, b: float) -> float` | Retorna o produto de `a` e `b`.                                  | `Calculadora.multiplicar(4, 2.5)  # → 10.0` |
| `dividir`     | `dividir(a: float, b: float) -> float`     | Retorna a divisão `a / b`. Levanta `ValueError` se `b` for zero. | `Calculadora.dividir(10, 2)  # → 5.0`       |

#### Detalhes dos métodos

```python
@staticmethod
def somar(a: float, b: float) -> float:
    """Retorna a soma de *a* e *b*.

    >>> Calculadora.somar(2, 3)
    5
    """
    return a + b
```

```python
@staticmethod
def subtrair(a: float, b: float) -> float:
    """Retorna a diferença entre *a* e *b* (a - b).

    >>> Calculadora.subtrair(5, 2)
    3
    """
    return a - b
```

```python
@staticmethod
def multiplicar(a: float, b: float) -> float:
    """Retorna o produto de *a* e *b*.

    >>> Calculadora.multiplicar(4, 2.5)
    10.0
    """
    return a * b
```

```python
@staticmethod
def dividir(a: float, b: float) -> float:
    """Retorna a divisão de *a* por *b*.

    Levanta ``ValueError`` se *b* for zero para evitar ``ZeroDivisionError``
    não tratado.

    >>> Calculadora.dividir(10, 2)
    5.0
    """
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b
```

---

## Guia rápido de uso

```python
# Importando a classe
from calculadora import Calculadora

# Operações básicas
soma = Calculadora.somar(10, 5)          # 15
sub = Calculadora.subtrair(10, 5)        # 5
mult = Calculadora.multiplicar(4, 2.5)   # 10.0

# Divisão segura
try:
    div = Calculadora.dividir(10, 0)
except ValueError as e:
    print(e)  # "Divisão por zero não é permitida."
```

---

## Considerações de design

- **Métodos estáticos**: Facilita o uso da classe como um namespace de funções utilitárias, sem necessidade de instanciar objetos.
- **Type hints**: Melhoram a legibilidade e permitem que ferramentas de análise estática (mypy, pyright) detectem inconsistências de tipo.
- **Tratamento de erro**: A divisão por zero gera um `ValueError` com mensagem clara, evitando o `ZeroDivisionError` padrão que poderia ser menos amigável ao usuário da API.

---

## Licença

Este código está sob a licença MIT (ou outra que você preferir). Consulte o arquivo `LICENSE` do projeto para mais detalhes.
