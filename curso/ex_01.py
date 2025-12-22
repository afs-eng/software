
dados = (
    {1: 'Sinto - me estranho e não sei por quê'},
    {2: 'Sinto vontade de ficar longe das pessoas da minha casa'},
    {3: 'Sinto vontade de ficar longe dos meus amigos'},
    {4: 'Estou mais agressivo'},
    {5: 'Sinto - me culpado'},
    {6: 'Viver está sendo difícil para mim'},
    {7: 'Choro'},
    {8: 'Sinto - me triste'},
    {9: 'Tenho vontade de fazer as coisas que gosto'},
    {10: 'Sinto - me sozinho'},
    {11:'Prefiro estar só'},
    {12: 'Acredito em um futuro bom'},
    {13: 'Meus dias têm sido bons'},
    {14: 'Tenho planos para o futuro'},
    {15: 'Tenho dormido bem'},
    {16: 'Acredito nas minhas capacidades'},
    {17: 'Estou feliz com minha vida'},
    {18: 'Consigo me concentrar nas minhas tarefas'},
    {19: 'Gosto de mim como eu sou'},
    {20: 'Tenho me sentido mal, sem estar doente'},
    {21: 'Penso em me machucar de propósito'},
    {22: 'Penso em me matar'},
    {23: 'Tenho comido normalmente'},
    {24: 'Sinto - me sem energia'},
    {25: 'Sinto - me feio'},
    {26: 'Sinto que as pessoas não querem estar comigo'}
)


x = []
# Lista dos itens com correção normal
itens_branco = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 20, 21, 22, 24, 26, 27]

# Lista dos itens com correção invertida (resposta corrigida = 2 - resposta)
itens_azul = [9, 12, 13, 14, 15, 16, 17, 18, 19, 23, 25]



respostas = []

for i in range(1, 27):
    while True:
        try:
            x = int(input(f'Item {i}: '))
            if x in [0, 1, 2]:
                respostas.append(x)
                break
            else:
                print('digite um valor errado')
        except ValueError:
            print('digite um valor errado')

for i in enumerate(respostas):
    print(f'Resposta: {i}')

pontuacao_total = []

for i in range(1, 27):
    original = respostas[i -1]
    if i in itens_azul:
        corrigido = 2 - original
    else:
        corrigido = original
    pontuacao_total.append(corrigido)

print(pontuacao_total)















































