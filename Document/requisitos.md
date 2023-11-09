# Requisitos do sistema

### Requisitos funcionais
1. (RF001) - O sistema deve sortear uma letra do alfabeto e retornar ao usuário, além de garantir que essa letra não se repita no sorteio.
2. (RF002) - O sistema deve fornecer um histórico de letras já sorteadas.
3. (RF003) - O sistema deve limpar a sessão e redirecionar para a página inicial, somente quando selecionado a opção de **_Encerrar partida_**.

### Requisitos não funcionais
1. (RNF001) - O sistema tem que retornar a letra sorteada em 5 segundos.
2. (RNF002) - O sistema é construido com as seguintes tecnologias:
    * Python
    * Flask
    * HTML
    * CSS
    * JavaScript

### Regras de negócio
1. (RN001) - O sistema poderá sortear apenas 26 vezes, número correspondente a quantidade de letras do alfabeto.
