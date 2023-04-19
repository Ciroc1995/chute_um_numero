import random


print('Seja bem-vindo ao jogo "Chute o número: Que número eu pensei?" ')
input('Aperte enter para iniciar o programa...')
print('Iniciando')


print('foi gerado um número entre 1 e 100...')
numero_secreto = random.randint(1, 101)

while True:
    chute = int(input('Chute um número de 1 a 100: '))

    if chute > numero_secreto:
        print('Chute um número menor')
        continue
    elif chute < numero_secreto:
        print('Chute um número maior')
        continue
    elif chute == numero_secreto:
        print(f'PARABÉNS! VOCÊ CHUTOU O VALOR CERTO: {numero_secreto}')

    jogar_novamente = input(
        'Jogo encerrando, gostaria de jogar novamente? (s/n)')
    if jogar_novamente == 's':
        numero_secreto = random.randint(1, 101)
        print('-------------------------------------')
        print('foi gerado um número entre 1 e 100...')
        continue
    if jogar_novamente == 'n':
        print('-------------------------------------')
        print('Encerrando o jogo...')
        print('-------------------------------------')
        input('Aperta qualquer tecla para continuar...')
        continue
