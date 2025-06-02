import random
from time import sleep


def escreva(msg):
    print('\033[0;36m' + '~' * len(msg))
    print(msg)
    print('~' * len(msg) + '\033[m')


nome = input('\033[0;33mDigite o nome da sua aventura:\033[m ').upper()
escreva(nome)

print('\n\033[0;34mA aventura começa em...\033[m')
for c in range(5, 0, -1):
    print(f'\033[0;35m{c}\033[m')
    sleep(1)
print('\033[0;34m' + '=' * 50 + '\033[m')


classes = {
    'Guerreiro': {'vida': 100, 'ataque': 15, 'defesa': 8},
    'Mago': {'vida': 70, 'ataque': 20, 'defesa': 4},
    'Arqueiro': {'vida': 85, 'ataque': 17, 'defesa': 6}
}

locais = {
    'Floresta': {'inimigo': ('Lobo', 30, 8, 2), 'chefao': ('Rei Goblin', 70, 14, 5), 'feito': False},
    'Caverna': {'inimigo': ('Morcego Gigante', 35, 9, 2), 'chefao': ('Senhor dos Orcs', 80, 16, 6), 'feito': False},
    'Castelo': {'inimigo': ('Esqueleto', 40, 10, 3), 'chefao': ('Cavaleiro Sombrio', 90, 18, 7), 'feito': False}
}


def batalha(player, inimigo):
    nome, vida, atk, defe = inimigo
    print(f"\n👾 \033[0;31m{nome} apareceu!\033[m")

    while player['vida'] > 0 and vida > 0:
        print(f"\n❤️ Sua vida: \033[0;32m{player['vida']}\033[m | 👾 Vida do {nome}: \033[0;31m{vida}\033[m")
        acao = input("\033[0;33m1 - Ataque ⚔️  |  2 - Habilidade 💥 👉 \033[m")

        if acao == '1':
            dano = max(player['ataque'] - defe, 0)
            vida -= dano
            print(f"⚔️ \033[0;32mVocê causou {dano} de dano.\033[m")
        elif acao == '2':
            dano = {'Guerreiro': player['ataque'] * 2 - defe,
                    'Mago': 25,
                    'Arqueiro': player['ataque']}[player['classe']]
            dano = max(dano, 0)
            vida -= dano
            print(f"💥 \033[0;35mHabilidade causou {dano} de dano.\033[m")

        if vida > 0:
            dano_inimigo = max(atk - player['defesa'], 0)
            player['vida'] -= dano_inimigo
            print(f"👊 \033[0;31m{nome} te causou {dano_inimigo} de dano.\033[m")

    if player['vida'] > 0:
        print(f"✅ \033[0;32mVocê derrotou {nome}!\033[m")
        return True
    else:
        print(f"❌ \033[0;31mFoi derrotado por {nome}.\033[m")
        return False


print("\n\033[0;36mEscolha sua classe:\033[m")
for i, c in enumerate(classes, 1):
    print(f"\033[0;33m{i} - {c}\033[m")

while True:
    try:
        opc = int(input("👉 "))
        if 1 <= opc <= len(classes):
            classe = list(classes.keys())[opc - 1]
            player = classes[classe].copy()
            player['classe'] = classe
            break
        else:
            print("\033[0;31m❌ Escolha inválida.\033[m")
    except:
        print("\033[0;31m❌ Digite um número.\033[m")
