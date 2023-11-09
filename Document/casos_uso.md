# Casos de uso
1. **O usuário acessa a página inicial do sistema e vai encontrar um link para iniciar o sorteador, e em seguida encontrar um menu com as seguintes opções:**
    * **_Sortear Letra_**
    * **_Ver letras sorteadas_**
    * **_Encerrar partida_**
2. **O usuário escolhe a opção de sortear letra.**
    * _O sistema vai exibir um contador de 5 segundos e retornar a letra sorteada no backend, e verá dois links, sendo eles:_
      * **_Ver as letras sorteadas_**
      * **_Voltar ao menu_**
  * _Paralelamente, no backend será sorteado a letra, e adicionada em um vetor com as letras já sorteadas._
3. **O usuário escolhe a opção de Ver letras sorteadas.**
    * _O sistema vai exibir as letras já sorteadas na ordem em que foram sorteadas, e verá dois links, sendo eles:_
      * **_Sortear letra_**
      * **_Voltar ao menu_**
4. **O usuário decide encerrar a partida.**
    * _O sistema vai retornar para a página inicial e limpar os dados da sessão._
5. **Quando todas as letras do alfabeto forem sorteadas, o usuário será redirecionado para a página de histórico toda vez que tentar sortear letra nessa condição.**
