
import time

votos_bolsonaro = 0
votos_lula = 0
x = 0
X = 0

while True:
    print()
    print(f'\033[1;42;36m Total de votos de Bolsonaro:\033[m '
          f'{votos_bolsonaro}\n')

    print(f'\033[1;41;36m Total de votos de Lula:\033[m'
          f' {votos_lula}\n')
    try:
        voto =int(input(f'Votação presidencial: '
                        f'\n1 - Bolsonaro\n2 - Lula\nx - Apurar\n'
                        f'\nA sua votação: '))
        if voto ==1:
            votos_bolsonaro = votos_bolsonaro + 1
        elif voto ==2:
            votos_lula = votos_lula + 1
        else:
            print("Digite apenas 1 ou 2 ")
            pass
    except:

        if voto == x or X:
            print()

        elif votos_bolsonaro > votos_lula:
            print("\n"*20)

            print(f'\033[0;32;40m Bolsonaro Ganhou !\n\n\n')
            break
        elif votos_bolsonaro < votos_lula:
            print("\n"*20)            

            print(f'\033[0;31;40m Lula Ganhou !\n\n\n')
            break

        votos_bolsonaro == votos_lula
        print("\n"*20)        
        print("EMPATOU !\n")
        time.sleep(2)
        print("Vai ter Segundo Turno !\n\n")

        break
