from random import randint
from time import sleep

pontos = 0
quant_perguntas = 0
lista_inputs = []

inputs_possiveis = ['0', '1', '2', '3', '4', '5', '6', '7', '8', 'pronto']
escalaRelativa5 = ['C', 'Am', 'G', "Em", 'D', 'Bm', 'A', 'F#m', 'E', 'C#m', 'B', 'G#m', 'F#', 'D#m', 'C#', 'A#m', 'C'] #0
escalaRelativa4 = ['C', 'Am', 'F', 'Dm', 'Bb', 'Gm', 'Eb', 'Cm', 'Ab', 'Fm', 'Db', 'Bbm', 'Gb', 'Ebm', 'Cb', 'Abm', 'C'] #1
cadenciaPlagal = []  # 2
cadenciaAutentica = ['C', 'G', 'D', 'A', 'E', 'B', 'F', 'C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#', 'F#', 'C#', 'G#', 'D#', 'A#', 'F']  # 3
substitutoDireto = []  # 4
substitutoIndireto = []  # 5
campoharmonico = []  # 6
progressaoMaior = ['Dm7', 'G7', 'C7M', 'Gm7', 'C7', 'F7M', 'Cm7', 'F7', 'Bb7M', 'Fm7', 'Bb7', 'Eb7M', 'Bbm7', 'Eb7', 'Ab7M', 'Ebm7', 'Ab7', 'Db7M', 'Abm7', 'Db7', 'Gb7M', 'Dbm7', 'Gb7', 'B7M', 'Gbm7', 'B7', 'E7M', 'Bm7', 'E7', 'A7M', 'Em7', 'A7', 'D7M', 'Am7', 'D7', 'G7M']
progressaoMenor = []  # 8

tupla = escalaRelativa5, escalaRelativa4, cadenciaAutentica, cadenciaPlagal, substitutoDireto, substitutoIndireto, campoharmonico, progressaoMaior, progressaoMenor

print('''{}\n\033[32m✨ BEM VINDO AO QUIZ SOBRE TEORIA MUSICAL ✨\033[m\n{}\n\033[36mEscolha o conteúdo do seu quiz\033[m
\033[m[ \033[35m0\033[m ] Escalas Relativas, ciclo de quinta ( # )
\033[m[ \033[35m1\033[m ] Escalas Relativas, ciclo de quarta ( b )
\033[m[ \033[35m2\033[m ] Cadência Plagal
\033[m[ \033[35m3\033[m ] Cadência Autêntica ( # )
\033[m[ \033[35m4\033[m ] Substituto Direto
\033[m[ \033[35m5\033[m ] Substituto Indireto
\033[m[ \033[35m6\033[m ] Campo Harmônico
\033[m[ \033[35m7\033[m ] Progressão Maior
\033[m[ \033[35m8\033[m ] Progressão Menor
\033[m[ \033[35m9\033[m ] Todos os anteriores
\033[mEscreva \033[34mpronto\033[m para começar
\033[mEscreva \033[34mpontos\033[m para ver sua pontuação'''.format('-=-' * 15, '-=-' * 15))

while True:
    input_usuario = input('').strip()
    if inputs_possiveis.count(input_usuario) != 0:
        if input_usuario == 'pronto':
            break
        elif input_usuario.count('9') != 0:
            input_usuario = inputs_possiveis
            break
        else:
            lista_inputs.append(input_usuario)
    else:
        print('\033[31mValor inválido, tente novamente\033[m')

while True:
    if lista_inputs.count('0') != 0:
        relativas = randint(0, 15)
        resposta = input(f'Qual é a escala relativa de {escalaRelativa5[relativas]}?\n\033[33m')
        if resposta == 'pontos':
            print('\033[mAté agora, vc acertou \033[34m{}/{}\033[m questões'.format(pontos, quant_perguntas))
            continue
        if resposta == escalaRelativa5[relativas + 1] or resposta == escalaRelativa5[relativas - 1]:
            print('\033[32mCorreto\033[m')
            quant_perguntas += 1
            pontos += 1
        else:
            print('\033[31mIncorreto\033[m')
            quant_perguntas += 1
    elif lista_inputs.count('1') != 0:
        relativas = randint(0, 15)
        resposta = input(f'\033[mQual é a escala relativa de {escalaRelativa4[relativas]}?\n\033[33m')
        if resposta == 'pontos':
            print('\033[mAté agora, vc acertou \033[34m{}/{}\033[m questões'.format(pontos, quant_perguntas))
            continue
        if resposta == escalaRelativa4[relativas + 1] or resposta == escalaRelativa4[relativas - 1]:
            print('\033[32mCorreto\033[m')
            quant_perguntas += 1
            pontos += 1
        else:
            print('\033[31mIncorreto\033[m')
            quant_perguntas += 1
    elif lista_inputs.count('3') != 0:
        cadAUTEN = randint(0, 23)
        if cadAUTEN % 2 != 0:
            cadAUTEN += 1
        print(f'A pergunta sobre cadência autêntica seria aqui. Número gerado: {cadAUTEN}')
        resposta = input('Qual é a cadência correta? ')
        if resposta == 'pontos':
            print(f'\033[mAté agora, vc acertou \033[34m{pontos}/{quant_perguntas}\033[m questões')
            continue
        # Aqui você deve comparar a resposta do usuário com a cadência correta
        if resposta == cadenciaAutentica[cadAUTEN]:
            print('\033[32mCorreto\033[m')
            quant_perguntas += 1
            pontos += 1
        else:
            print('\033[31mIncorreto\033[m')
            quant_perguntas += 1
    # Adicione mais condições elif para as outras opções do quiz