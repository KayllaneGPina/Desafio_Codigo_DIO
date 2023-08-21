## Desafio 1
O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. Conferir se um texto vai caber em um tuíte é sua tarefa.

## Entrada
A entrada é uma linha de texto T (1 ≤ |T| ≤ 500).

## Saída
A saída é dada em uma única linha. Ela deve ser "TWEET" (sem as aspas) se a linha de texto T tem até 140 caracteres. Se T tem mais de 140 caracteres, a saída deve ser "MUTE".

## Exemplos
|Exemplo de Entrada|Exemplo de Saída|
|-------|-----|
|RT @TheEllenShow: If only Bradley's arm was longer. Best photo ever. #oscars pic.twitter.com/C9U5NOtGap   |TWEET|

---

## Desafio 2
Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

## Entrada
A entrada contém um único valor inteiro.

## Saída
Imprima por extenso o nome do mês correspondente ao número existente na entrada, com a primeira letra em maiúscula.

## Exemplos
|Exemplo de Entrada|Exemplo de Saída|
|-------|-----|
|4|April|

---

## Desafio 3
Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.

## Entrada
A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.

## Saída
Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor, confome exemplo abaixo.

## Exemplos
|Exemplo de Entrada|Exemplo de Saída|
|-------|-----|
|4|encaixa|
|56234523485723854755454545478690 78690|nao|
|5434554 543|encaixa|
|1243 1243|encaixa|
|54|nao|
|64545454545454545454545454545454554|encaixa|