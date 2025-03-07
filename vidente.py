print ('*********************************************')
print ('Bem vindo ao Vidente, seu jogo de adivinhação')
print ('*********************************************')

numero_secreto = 7
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print (f'Tentativa {rodada} de {total_de_tentativas}')
    chute = int(input('Digite o seu número'))

    acertou = chute == numero_secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto


    print (f'Você  digitou {chute} ')

    if(acertou):
     print('Você acertou! Parabéns, tu é vidente.')
    else:
        if(chute_maior):
           print('Você errou! Seu número foi maior do que o número secreto')
        elif(chute_menor):
            print('De vidente não tem nada <3, seu número é menor do que o número secreto.')

    rodada = rodada + 1


print('@@@@@@@@@@@')
print('Fim de jogo')
print('@@@@@@@@@@@')
