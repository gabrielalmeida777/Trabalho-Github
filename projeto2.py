while True:
    print('\n\033[0;34m' + '=' * 50 + '\033[m')
    print("\033[0;36m🏰 Onde deseja ir?\033[m")

    locais_lista = list(locais.keys())
    for i, loc in enumerate(locais_lista, 1):
        status = '\033[0;31m❌ (Explorado)\033[m' if locais[loc]['feito'] else ''
        print(f"\033[0;33m{i} - {loc} {status}\033[m")
    print(f"\033[0;33m{len(locais_lista)+1} - Vila (Curar)\033[m")

    try:
        escolha = int(input("👉 "))
    except:
        print("\033[0;31m❌ Digite um número válido.\033[m")
        continue

    if escolha == len(locais_lista) + 1:
        player['vida'] = classes[player['classe']]['vida']
        print("\033[0;32m❤️ Curado na vila!\033[m")
        continue

    if 1 <= escolha <= len(locais_lista):
        nome_local = locais_lista[escolha - 1]
        if locais[nome_local]['feito']:
            print("\033[0;31m⚠️ Já explorou esse local.\033[m")
            continue

        if not batalha(player, locais[nome_local]['inimigo']):
            print("\n\033[0;31m💀 GAME OVER!\033[m")
            break

        print("\n⚠️ ⚔️ \033[0;35mVocê encontrou o CHEFÃO!\033[m")
        if not batalha(player, locais[nome_local]['chefao']):
            print("\n\033[0;31m💀 GAME OVER!\033[m")
            break

        locais[nome_local]['feito'] = True
        print(f"\033[0;32m🎉 Você venceu em {nome_local}!\033[m")

        if all(locais[loc]['feito'] for loc in locais):
            print('\n🏆 \033[0;32mPARABÉNS! VOCÊ VENCEU TODOS OS DESAFIOS!\033[m')
            break
    else:
        print("\033[0;31m❌ Escolha inválida.\033[m")