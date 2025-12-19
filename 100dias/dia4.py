import random
pedra = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

papel = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

tesoura = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
# A escolha do usuário ainda é um texto (string):
# Escolha_usuário = input("...") 
opções = [pedra, papel, tesoura]

# Seu código para obter o movimento escolhido...
movimento_usuário = int(input("Bem vindo ao jogo! digite 1 para pedra, 2 para papel e 3 para tesoura"))- 1
escolha_computador = random.randint(0, 2)
print("Sua jogada:")
print(opções[movimento_usuário])

print("Jogada do Computador:")
print(opções[escolha_computador])
if movimento_usuário == escolha_computador:
    print("Houve um empate!")
elif movimento_usuário ==0 and escolha_computador ==2:
    print("você venceu!")
elif movimento_usuário > escolha_computador:
    print("você venceu")
else:
    print("você perdeu")