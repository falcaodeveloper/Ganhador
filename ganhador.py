#Desenvolvido por Ulisses F. Falcão em 21/01/2024

from random import choice

explicacao = 'Digite o nome de no mínimo 5 participantes para o sorteio.\nTecle ENTER após digitar o nome de cada participante.\nSe desejar sair e ver o ganhador, não digite o nome de ninguém e tecle ENTER.'
msnEntrada = 'Digite o nome do participante:\n'
msnSaida = 'É necessário, no minímo, 5 participantes.'
ganhador = 'Parabéns ao ganhador:\n {0}{1}{0}'
totParticipantes = 'Total de participantes: {}'
participante = []
cont = 0
print('=' * 80)
print(explicacao)
print('=' * 80)

while True:
    participante.append(input(msnEntrada))
    if participante[cont] == '':
        if len(participante) < 6:
            print(msnSaida)
            participante.remove('')
            cont -= 1
        else:
            participante.remove('')
            break
    cont += 1

print(ganhador.format('*' * 10, choice(participante)))
print(totParticipantes.format(len(participante)))