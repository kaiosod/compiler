# Compilador
#  Nome da linguagem: Mali

##  :dart: Objetivos

### Idéia da criação
Criação de uma linguagem para aprendizado que seja de fácil acesso no começo, e após isso dê ferramentas mais completas.

## :page_with_curl: Documentação

A especificação da linguagem está documentada no wiki do GitHub

## :key: Características

**Linguagem tipada** e **estruturada**, onde a mesma pode ter dois tipos de váriaveis e pode ser divida em pequenos blocos.

## :triangular_flag_on_post: Introdução rápida sobre a linguagem

### :pushpin: Hello World

```js
show('Hello World')
```

### :pushpin: Tipagem

liter -> Declara um conjunto de caracteres

#### Exemplo
```js
liter name = 'Mali'
```
numb -> Declara um numeral, podendo ser um numeral real ou inteiro

#### Exemplo
```js
numb year = 2022
```

#### Exemplo

boole -> representa o tipo boleano ou seja uma condição binaria que no caso da linguagem será true ou false.

```js
boole x = true
boole y = false
```
### :pushpin: Estrutura de Decisão: Declaração Case, Orcase e Other

Estruturas de decisão na lingugem Mali são usadas para verificar um comando e efetuar a decisão do mesmo. 
No exemplo a seguir, a condição ficará dentro do case e se atender a condição, irá realizar os comandos dentro do bloco case, caso não atenda, irá realzar os comandos do bloco other:

#### Exemplo

```js
case(x == 1):

  show('Atendeu o case')

other:

  show('Atendeu o other')


```

Também pode ser usado somente o case, e caso não atenda as condições, não irá realizar os comandos dentro do bloco somente:

#### Exemplo

```js

case(x == 1)

  show('Atendeu o case')


```

Dentro da condição pode conter um boole:

#### Exemplo

```js
boole condicao = true

case(condicao)

  show('Atendeu o case')

```

Caso precise de mais de uma condição, pode ser usado o orcase:

#### Exemplo

```js
case(x == 1):

  show('Atendeu o case')

orcase(x == 2):

  show('Atendeu o orcase')

other:

  show('Atendeu o other')
```

### :pushpin: Funções

A linguagem apresenta o conceito de funções. Funções são blocos de código que se propõe a realizar algum tipo de tarefa, podendo ser obtenção ou alteração de um valor específico ou um simples show.

#### Exemplo
```js
helloWorld():
  show('Hello World');
```
### :pushpin: Palavras Reservadas
A linguagem possui algumas palavras reservadas, que são palavras-chaves para usos de algumas funções;

#### Alguns Exemplos
```js
numb
liter
boole
if
else
true
false
null
show
doit
loop
case 
orcase
other
```

### :pushpin: Comentários
Comentários são importantes para indicar o que o trecho de código faz, documentação e outras, para comentar um código, basta colocar os simbolos // antes do comentário.

#### Exemplo
```js
printName():
//  show('Mali'); -> Trecho comentado
```

