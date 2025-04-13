# Quiz-de-Teoria-Musical

Este projeto é um quiz interativo sobre teoria musical, desenvolvido em Python. Ele permite que os usuários testem seus conhecimentos em diferentes tópicos relacionados à teoria musical, como escalas relativas, cadências e progressões harmônicas.

## Como funciona o código

1. **Inicialização**:
   - O programa começa importando as bibliotecas necessárias (`random` e `time`) e inicializando variáveis globais, como `pontos` (pontuação do usuário), `quant_perguntas` (quantidade de perguntas respondidas) e `lista_inputs` (lista de tópicos selecionados pelo usuário).

2. **Tópicos disponíveis**:
   - O quiz oferece os seguintes tópicos:
     - Escalas Relativas (ciclo de quinta e ciclo de quarta)
     - Cadência Plagal
     - Cadência Autêntica
     - Substituto Direto
     - Substituto Indireto
     - Campo Harmônico
     - Progressões Harmônicas (maior e menor)
   - O usuário pode escolher um ou mais tópicos digitando os números correspondentes no menu inicial.

3. **Interação inicial**:
   - O programa exibe um menu com as opções disponíveis e orienta o usuário a digitar `pronto` para começar o quiz ou `pontos` para verificar sua pontuação a qualquer momento.

4. **Execução do quiz**:
   - Após o usuário selecionar os tópicos e iniciar o quiz, o programa gera perguntas aleatórias com base nos tópicos escolhidos.
   - Para cada pergunta:
     - O programa exibe uma questão relacionada ao tópico selecionado.
     - O usuário deve digitar a resposta correta.
     - Caso o usuário digite `pontos`, o programa exibe a pontuação atual e continua o quiz.
     - A resposta do usuário é comparada com a resposta correta, e o programa informa se a resposta está correta ou incorreta, atualizando a pontuação e o número de perguntas respondidas.

5. **Tópicos implementados**:
   - **Escalas Relativas (ciclo de quinta e quarta)**:
     - O programa pergunta qual é a escala relativa de uma nota aleatória.
   - **Cadência Autêntica**:
     - O programa gera uma pergunta sobre cadências autênticas e verifica se a resposta do usuário está correta.
   - Outros tópicos podem ser implementados no futuro, seguindo a mesma estrutura.

6. **Finalização**:
   - O programa continua rodando até que o usuário decida encerrá-lo manualmente.

## Como executar o programa

1. Certifique-se de ter o Python instalado em sua máquina.
2. Baixe ou clone este repositório.
3. Execute o arquivo `code_teoria.py` no terminal:
   ```bash
   python code_teoria.py