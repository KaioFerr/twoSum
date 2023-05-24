# Two Sum
Este é um problema clássico de programação onde você precisa encontrar os índices de dois números em uma matriz que somam um alvo específico. O problema assume que cada entrada tem exatamente uma solução e que não é possível usar o mesmo elemento duas vezes.

## Descrição do Problema
Dada uma matriz de inteiros nums e um inteiro target, o objetivo é retornar os índices dos dois números de modo que eles somem target. Você pode supor que há sempre uma solução válida e que não há duplicatas na matriz de entrada.

## Código
``` python
class Solution:
    def twoSum(self, nums: List[int], target: int):
        num_dicionario = {}
        for i, num in enumerate(nums):
            complemento = target - num
            if complemento in num_dicionario:
                return (num_dicionario[complemento], i)
            num_dicionario[num] = i
            # ^ Adiciona o número atual e seu índice ao dicionário
        return None
```
## Exemplo
Considere o seguinte exemplo:

```python
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
```
