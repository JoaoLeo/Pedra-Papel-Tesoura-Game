from random import randint
from time import sleep
print("SUAS OPÇÕES:")
print("[0] PEDRA")
print("[1] PAPEL")
print("[2] TESOURA")
jogada = int(input("Qual sua jogada?"))
computador = randint(0,2)


sleep(1)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")

print("="*20)
if jogada ==0 and computador==2:
    print("O jogador jogou Pedra")
    print("O computador jogou Tesoura")
    print("O jogador vence!!!")

elif jogada ==0 and computador==1:
    print("O jogador jogou Pedra")
    print("O computador jogou Papel")
    print("O computador vence!!!")

elif jogada ==1 and computador==0:
    print("O jogador jogou Papel")
    print("O computador jogou Pedra")
    print("O jogador vence!!!")

elif jogada == 1 and computador==2:
    print("O jogador jogou Papel")
    print("O computador jogou Tesoura")
    print("O computador vence!!!")

elif jogada ==2 and computador==1:
    print("O jogador jogou Tesoura")
    print("O computador jogou Papel")
    print("O jogador vence!!!")

elif jogada ==2 and computador==0:
    print("O jogador jogou Tesoura")
    print("O computador jogou Pedra")
    print("O computador vence!!!")

elif jogada==computador:
    print("Ambos jogaram {}".format(jogada))
    print("Empate!")

else:
    print("Jogue uma opção acima")

print("="*20)