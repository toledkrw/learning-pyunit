# PyUnit
```
DISCLAIMER:
This repo was created to the sole purpose of studying the PyUnit framework.
```

## Introdução

### Testes unitários, o que são:

Softwares se tornaram um dos pilares do mundo contemporâneo, porém, esses pilares devem estar firmes para que tudo continue seguindo o caminho do progresso. De forma a verificar e garantir a integridade desses pilares, realizamos testes, para que tenhamos certeza que os softwares desenvolvidos estão funcionando de acordo com o desejado, e que tenham o mínimo possível de erros e defeitos.

Um dos testes realizados para termos essa garantia, são os **testes unitários**. 

Testes unitários buscam conferir a corretude do código em sua menor granularidade, ou seja, de forma mais interna possível. Geralmente, esses testes são realizados a nível de função, sejam funções globais ou mesmo métodos de classe; esperando que a função testada retorne o esperado no teste.

## História

### O que é o Pyunit:

(Muito provavelmente) Criado por *Steve Purcell*, e lançado em 23 de março de 2001; de acordo com a documentação oficial, o *Python Unit Testing Framework*, chamado de *PyUnit* por convenção, é uma versão Python do *JUnit*, o framework de testes unitários de Java que, por sua vez, é a versão Java do framework de testes de Smalltalk, de Kent.

O PyUnit foi criado com o intuito de trazer ao **Python** todos os recursos que já haviam no framework de teste unitário *JUnit*. 

A ferramenta evoluiu de forma a explorar plenamente os recursos da linguagem e se adequar ao jeito Python de escrever código.

## Configurações necessárias e Instalação

Em seu lançamento, *PyUnit* foi incluído na Biblioteca Padrão do Python, ou seja, é uma biblioteca interna padrão do Python, e está disponível desde a versão 2.1 do Python.

De acordo com a documentação oficial, *PyUnit* foi desenhado para funcionar em qualquer versão padrão do Python 1.5.2 e superiores.

Por ser utilizado nativamente como uma biblioteca, o *Pyunit* não precisa de nenhuma configuração prévia para executar os testes.

## Exemplo de código da ferramenta (Unittest)

De acordo com a documentação oficial, as classes necessárias para escrever os testes podem ser encontradas no modulo `unittest`.

Como esse módulo vem por padrão nas instalações Python desde a versão 2.1, basta importa-lo. Se estiver executando uma versão inferior a essa, você deve obter o módulo à partir de uma distribuição do *PyUnit* à parte, disponível no site SourceForge (o link está disponível na documentação do *PyUnit*).

No *PyUnit*, casos de teste são representados pela classe `TestCase`, disponível no módulo `unittest`. Para criar seu próprio caso de teste, você deve escrever subclasses à partir da `TestCase`.

Dentre os vários métodos disponíveis, podemos utilizar os métodos  `setUp()` e `tearDown()`. Sendo o `setUp()` para ser executado antes (para preparar) e o `tearDown()` depois do teste (para tratar alguma ocorrência).

Dentro desta camada de teste podemos utilizar asserções, para verificar a veracidade do código, presentes nos métodos: `assertEqual()`, `assertNotEqual()`, `assertTrue()`, dentre outros.

---

## Referências

- [http://pyunit.sourceforge.net/](http://pyunit.sourceforge.net/)
- [Tutorial de teste de unidade com python unittest](https://medium.com/tutorial-de-teste-de-unidade-com-python-unittest/tutorial-de-teste-de-unidade-com-python-unittest-5bf9b55ac6c8)
- [Teste unitário com pyunit devmedia](https://www.devmedia.com.br/teste-unitario-com-pyunit/41233)
- [https://www.devmedia.com.br/e-ai-como-voce-testa-seus-codigos/39478](https://www.devmedia.com.br/e-ai-como-voce-testa-seus-codigos/39478)